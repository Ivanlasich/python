def s_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    left = max(x1, x3);
    top = min(y2, y4);
    right = min(x2, x4);
    bottom = max(y1, y3);
    width = right - left;
    height = top - bottom;

    if (width < 0 or height < 0):
        return 0;

    return width * height;

def s(x1, y1, x2, y2):
    l = abs(x2 - x1)
    r =abs(y2-y1)
    return l*r


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

s1 = 0
s2 = 0
for i in range(0,n):
    s1 = s1 + s(a[i][0],a[i][1],a[i][2],a[i][3])
s2 = 0
for i in range(0,n):
    for j in range(i+1,n):
        s2 = s2 + s_intersection(a[i][0],a[i][1],a[i][2],a[i][3],a[j][0],a[j][1],a[j][2],a[j][3])

print(s1-s2)

