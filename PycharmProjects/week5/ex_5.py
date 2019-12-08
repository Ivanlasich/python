import requests
import base64
import json


'''
login='alladin'
password='opensesame'
url = ' https://datasend.webpython.graders.eldf.ru/submissions/1/'
headers={'Authorization': f'Basic {base64.b64encode(f"{login}:{password}".encode()).decode()}'}
r = requests.post(url, headers=headers)
print(r.text)
'''

login='galchonok'
password='ktotama'
url = ' https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/'
headers={'Authorization': f'Basic {base64.b64encode(f"{login}:{password}".encode()).decode()}'}
r = requests.put(url, headers=headers)
a = r.text
print(a)
one, two = a.split(":")
a = two[2:len(two)-2]
print(a)
with open('data.json', 'w') as f:
    json.dump(a, f)