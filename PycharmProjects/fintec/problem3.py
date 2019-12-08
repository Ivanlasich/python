def max(a,b):
    if (a>b):
        return a
    else:
        return b

def min(a,b):
    if (a<b):
        return a
    else:
        return b
nums1 = map(int, input().split())
nums1 = list(nums1)

nums2 = map(int, input().split())
nums2 = list(nums2)
a = nums1[0]
b = nums1[1]
c = nums2[0]
d = nums2[1]


if((max(d,c)>=max(a,b)) and (min(d,c)>=min(a,b))):
    print("YES")
else:
    print("NO")
