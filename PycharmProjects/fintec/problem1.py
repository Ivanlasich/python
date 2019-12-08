nums = map(int, input().split())
nums = list(nums)
n  = nums[0]
x1 = nums[1]
y1 = nums[2]
x2 = nums[3]
y2 = nums[4]
a = []
for i in range(n):
    a.append(i+1)

b = a[x1-1:y1]
b = b[::-1]

for i in range(x1-1,y1):
    a[i]= b[i-(x1-1)]

b = a[x2-1:y2]
b=b[::-1]

for i in range(x2-1,y2):
    a[i]= b[i-(x2-1)]

for i in a:
    print(i, end=" ")
