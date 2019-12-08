def search(s):
    l =len(s)
    if (l ==0):
        return 1
    if (l==1):
        return 1

    sum = int(s[0] + s[1])
    if(10<=sum<=33):

        return (search(s[2:])+search(s[1:]))
    else:
        return (search(s[1:]))


s = input()

print(search(s))

