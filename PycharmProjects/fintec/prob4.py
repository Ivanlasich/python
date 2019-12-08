def create(x1,y1,x2,y2):
    a = set()

    for i in range(y1,y2):
        for j in range(x1,x2):
            a.add((j+0.5,i+0.5))


    return a



a = []
n = int(input())
for i in range(n):
    nums = map(int, input().split())
    nums = list(nums)
    x1 = nums[0]
    y1 = nums[1]
    x2 = nums[2]
    y2 = nums[3]
    b = (x1,y1,x2,y2)
    a.append(b)
g = set()
for i in range(n):
    d = create(a[i][0], a[i][1],a[i][2],a[i][3])
    g = g.union(d)
print(len(g))
