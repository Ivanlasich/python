import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.animation import FuncAnimation

t, r = sp.symbols('t r')
EPS = 1e-12


class ImpulseTask:

    def __init__(self, analytic, alpha, L, T, h, tau, from_, to):
        self.from_ = from_  # impulse start
        self.to = to  # impulse end

        self.L = L
        self.T = T
        self.alpha = alpha
        self.sym_f = (analytic.diff(t, 2) - self.alpha ** 2
                      * (analytic.diff(r)).diff(r))
        self.f = sp.lambdify((t, r), self.sym_f)

        self.h = h
        self.tau = tau

        self.n_r_dots = 2 + int(L / h)
        self.n_t_dots = 2 + int(T / tau)

        self.r_space = np.arange(self.n_r_dots) * self.h - self.h / 2
        self.t_space = np.arange(self.n_t_dots) * self.tau


class ImpulseConvergenceTest:

    def __init__(self, analytic, L, T, from_, to, alpha, min_r_dots, tau_coefficient, tau_power):
        min_r_segments = min_r_dots - 2
        self.analytic = analytic
        h_max = L / min_r_segments
        h_list = np.array([h_max / 3 ** i for i in range(3)])
        tau_list = tau_coefficient * h_list ** tau_power

        self.tau_power = tau_power

        self.tasks = [ImpulseTask(analytic=analytic,
                                  alpha=alpha,
                                  L=L, T=T,
                                  h=h_list[i],
                                  tau=tau_list[i],
                                  from_=from_,
                                  to=to) for i in range(3)]
        for task in self.tasks:
            print('Cournt: {}'.format(task.tau / task.h * task.alpha))
            print('tau / h^2: {}\n'.format(task.tau / task.h ** 2))
        self.results = []

    def compute(self, next_step):
        divider = 3 ** self.tau_power

        for i, task in enumerate(self.tasks):

            def is_saving(n):
                if n % divider ** i == 0:
                    print('saving t: {:.4}'.format(self.tasks[i].t_space[n]))
                    return True
                return False

            u = initialize_array(self.tasks[i], self.analytic)
            result = compute(task, u=u, is_saving=is_saving, next_step=next_step)
            self.results.append(result)
            print('done {}/3'.format(i + 1))
        pass

    def plot(self, expected):
        len_ = min(len(self.results[0]), len(self.results[1]), len(self.results[2]))
        conv_order_C_norm = np.ndarray((len_,))
        conv_order_L2_norm = np.ndarray((len_,))
        for i in range(len_):
            results_t = tuple(map(lambda r: r[i], self.results))
            conv_order_C_norm[i], conv_order_L2_norm[i] \
                = calculate_convergence_orders_3_grids(numeric_solutions=results_t,
                                                       h=self.tasks[0].h,
                                                       d=1)

        fig = plt.figure()
        plt.plot(self.tasks[0].t_space[:-1], conv_order_C_norm, label='C norm')
        plt.plot(self.tasks[0].t_space[:-1], conv_order_L2_norm, label='L2 norm')
        plt.plot([0, self.tasks[0].t_space[-2]], [expected, expected], label='Reference')
        plt.xlabel('time, s')
        plt.ylabel('convergence')
        fig.suptitle('Convergence by 3 dots: dim = 1, function - gauss distribution')
        plt.legend()
        plt.show()


def projection_without_bounds(better_grid, worse_grid):
    better_grid = np.asanyarray(better_grid)
    worse_grid = np.asanyarray(worse_grid)

    grid_multiplier = 3
    skipped_dots = 2

    diff = int(np.log((better_grid.shape[0] - skipped_dots) / (worse_grid.shape[0] - skipped_dots))
               / np.log(grid_multiplier))
    sep = int(grid_multiplier ** diff)

    res = better_grid
    # some indices should be skipped
    passed = math.ceil(3 ** diff / 2)
    res = res[passed:-passed:sep]

    return res


def calculate_convergence_orders_3_grids(numeric_solutions: tuple, h, d):
    def projection_on_worst_grid(numeric_solutions):
        return [projection_without_bounds(u, numeric_solutions[0]) for u in numeric_solutions]

    def norm_C(vector):
        return abs(vector).max()

    def norm_L2(vector, h, d):
        return np.sqrt(np.sum(h ** d * vector ** 2))

    factors_C_norm = []
    factors_L2_norm = []
    for i in range(1, len(numeric_solutions) - 1):
        three_indices = (i - 1, i, i + 1)
        results = [numeric_solutions[i] for i in three_indices]
        u_on_h_list = projection_on_worst_grid(results)

        factor_C_norm = norm_C(u_on_h_list[0] - u_on_h_list[1]) / (norm_C(u_on_h_list[1] - u_on_h_list[2]) + EPS)
        factors_C_norm.append(factor_C_norm)

        factor_L2_norm = (norm_L2(u_on_h_list[0] - u_on_h_list[1], h=h, d=d)
                          / (norm_L2(u_on_h_list[1] - u_on_h_list[2], h=h, d=d) + EPS)
                          )
        factors_L2_norm.append(factor_L2_norm)

    return np.array(factors_C_norm), np.array(factors_L2_norm)


def initialize_array(config, analytic):
    u = np.zeros((3, config.n_r_dots))

    f_analytic_0 = sp.lambdify(r, analytic.subs(t, 0))
    f_analytic_1 = sp.lambdify(r, analytic.subs(t, config.tau))

    u[0] = f_analytic_0(config.r_space)
    u[1] = f_analytic_1(config.r_space)

    # keeping only one impulse
    impulse_indices = np.logical_and(config.r_space >= config.from_, config.r_space <= config.to)
    u[0][np.logical_not(impulse_indices)] = 0
    u[1][np.logical_not(impulse_indices)] = 0
    return u


def next_step_O42(config, u: np.ndarray, n: int):
    alpha = config.alpha
    h = config.h
    tau = config.tau
    uf, uc, up = u[1, 3:-1], u[1, 2:-2], u[1, 1:-3]
    uff, upp = u[1, 4:], u[1, :-4]

    space_op_result = (alpha / h) ** 2 * (uf - 2 * uc + up - 1 / 12 * (uff - 4 * uf + 6 * uc - 4 * up + upp))
    u[2, 2:-2] = (2 * uc - u[0, 2:-2] + tau ** 2
                  * (space_op_result + config.f(config.t_space[n], config.r_space[2:-2])))
    # setting boundary conditions
    # assuming that impulse does not come close to the bound
    u[2, :2] = u[2, 3]
    u[2, -2:] = u[1, -3]


def next_step_O62(config, u: np.ndarray, n: int):
    alpha = config.alpha
    h = config.h
    tau = config.tau
    uf, uc, up = u[1, 4:-2], u[1, 3:-3], u[1, 2:-4]
    uff, upp = u[1, 5:-1], u[1, 1:-5]
    ufff, uppp = u[1, 6:], u[1, :-6]

    space_op_result = (alpha / h) ** 2 * (-49/36 * 2 * uc + 3/2 * (uf + up) -3/20 * (uff + upp) + 1/90 * (ufff + uppp))
    u[2, 3:-3] = (2 * uc - u[0, 3:-3] + tau ** 2
                  * (space_op_result + config.f(config.t_space[n], config.r_space[3:-3])))
    # setting boundary conditions
    # assuming that impulse does not come close to the bound
    u[2, :3] = u[2, 4]
    u[2, -3:] = u[1, -4]


def compute(c, u, is_saving, next_step):
    def cyclic_shift(u: np.ndarray, start: int, stop: int):
        yield start, u
        for n in range(start + 1, stop):
            u = np.roll(u, -1, axis=0)
            yield n, u

    n = 0
    results = []

    for n, u in cyclic_shift(u, 0, c.n_t_dots - 1):
        if is_saving(n):
            results += [u[0].copy()]
        next_step(c, u, n)

    if is_saving(n + 1):
        results += [u[-1].copy()]
    return results


def animate_2d(x_data, y_data):
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'b', label='Numeric', lw=2)
    line_analytic, = ax.plot([], [], 'r', label='Analytic', lw=2)
    ax.grid()

    def init():
        ydata = y_data[-1]
        ax.set_ylim(ydata.min(), ydata.max())
        ax.set_xlim(0, x_data[-1])
        line.set_data(x_data, ydata)
        return line_analytic, line

    def run(i):
        ydata = y_data[i]
        ymin, ymax = ax.get_ylim()
        if ydata.max() > ymax:
            ymax = ydata.max()
        if ydata.min() < ymin:
            ymin = ydata.min()

        ax.set_ylim(ymin, ymax)
        line.set_data(x_data, ydata)

        return line_analytic, line

    ani = FuncAnimation(fig, run, blit=False, interval=50,
                        repeat=True, init_func=init, frames=len(y_data))
    plt.legend(loc=2)
    plt.show()


def run_O42():
    L = 6
    T = 2
    alpha = .5
    analytic = sp.exp(-(r - alpha * t - 2.5) ** 2 * 4)

    test = ImpulseConvergenceTest(analytic=analytic, L=L, T=T, alpha=alpha,
                              min_r_dots=42, tau_coefficient=4, tau_power=2,
                              from_=0, to=6)
    test.compute(next_step_O42)

    # watch animated solutions

    # animate_2d(test.tasks[0].r_space, test.results[0])
    # animate_2d(test.tasks[1].r_space, test.results[1])
    # animate_2d(test.tasks[2].r_space, test.results[2])

    test.plot(expected=3 ** 4)


def run_O62():
    L = 6
    T = 2
    alpha = .5
    analytic = sp.exp(-(r - alpha * t - 2.5) ** 2 * 4)

    test = ImpulseConvergenceTest(analytic=analytic, L=L, T=T, alpha=alpha,
                              min_r_dots=42, tau_coefficient=4, tau_power=3,
                              from_=0, to=6)
    test.compute(next_step_O62)

    # watch animated solutions

    # animate_2d(test.tasks[0].r_space, test.results[0])
    # animate_2d(test.tasks[1].r_space, test.results[1])
    # animate_2d(test.tasks[2].r_space, test.results[2])

    test.plot(expected=3 ** 6)
    pass


if __name__ == '__main__':
    run_O42()