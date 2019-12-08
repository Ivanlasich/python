import json


d = {}
a ={'longitude': 39.522207, 'latitude': 55.929065}
d[1] = a;
d[2] = a;
with open('data.json', 'w') as f:
    json.dump(d, f)
s = {}

with open('data.json') as f:
    s = json.load(f)
print(s)