import requests
import base64
import json


login='galchonok'
password='ktotama'
url = 'https://smarthome.webpython.graders.eldf.ru/api/auth.current'
url1 = 'https://smarthome.webpython.graders.eldf.ru/api/user.controller'

headers={'Authorization': 'Bearer 02d9df36cf83ef0613adf067ea3c80b5f2ad1b88ca01a4988fc0a73e6b2a4a8e'}
r = requests.get(url1, headers=headers)
print(r.text)
