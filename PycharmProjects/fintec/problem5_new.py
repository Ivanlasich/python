def fib(n):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1

    return (fib2)

inc = 0;
s=input()
for i in range(len(s)-1):
    a = int(s[i]+s[i+1])
    if (10<=a<=33):
        inc=inc+1
print(fib(inc+2))