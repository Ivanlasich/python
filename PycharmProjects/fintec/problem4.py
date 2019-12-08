def sq(a):
    b = len(a)
    s = 1
    if (b == 4):
        return s
    a = int((b - 4)/2 + 0.5)
    s = s + a
    return s

def create(x1,y1,x2,y2):
    a = set()
    y1 = min(y1,y2)
    y2 = max(y1,y2)
    x1= min(x1,x2)
    x2 =max(x1,x2)

    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            a.add((j,i))


    return a


nums = map(int, input().split())
nums = list(nums)
x1=nums[0]
y1=nums[1]
x2=nums[2]
y2=nums[3]
a =create(x1,y1,x2,y2)

print(sq(a))