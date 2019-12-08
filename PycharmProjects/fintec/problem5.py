def search(l):
    if (l==0):
        return 1
    if (l==1):
        return 1
    return(search(l-2)+search(l-1))

print(search(4))
s=input()
a = s.split('0')
sum =1
for i in a:
    sum = sum * search(len(i))
print(sum)

