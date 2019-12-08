import requests
import re

def calc_age(uid):
    d = {}
    token = '2986367029863670298636705329ea9b2a229862986367074e86bb3e7cc5444763657d6'
    version = 5.71
    id = uid
    response = requests.get('https://api.vk.com/method/users.get',
                            params={'v': version, 'access_token': token, 'user_ids': id})
    data = response.json()['response']
    data = data[0]['id']
    res = requests.get('https://api.vk.com/method/friends.get',
                       params={'v': version, 'access_token': token, 'user_id': data, 'fields': 'bdate'})
    data = res.json()['response']['items']
    for item in data:
        if 'bdate' in item:
            if re.findall((r'(\d+.\d+.\d+)'), item['bdate']):
                s = int(item['bdate'][item['bdate'].rfind('.') + 1:])
                a = 2019 - s
                d[a] = 0
    for item in data:
        if 'bdate' in item:
            if re.findall((r'(\d+.\d+.\d+)'), item['bdate']):
                s = int(item['bdate'][item['bdate'].rfind('.') + 1:])
                a = 2019 - s
                d[a] = d[a] + 1
    arr = []
    for item in d:
        arr.append((item, d[item]))
    arr.sort(key=lambda x: x[0])
    arr.reverse()
    arr.sort(key=lambda x: x[1])
    arr.reverse()
    return arr


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)