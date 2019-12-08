import re
s=input()

pattern = r'[a-zA-Z]'
a =re.findall(pattern, s.lower())
if(list(a) == list(reversed(a))):
    print('YES')
else:
    print('NO')
