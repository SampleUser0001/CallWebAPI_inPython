# -*- coding: utf-8 -*-
import requests

URL = 'http://zipcloud.ibsnet.co.jp/api/search'
params = {'zipcode':'2500011'}
ITEM_KEY = 'results'
KEYS = ['address1','address2','address3']

result = requests.get(URL, params=params).json()

print(result[ITEM_KEY])

for items in result[ITEM_KEY]:
    for key in KEYS:
        print(key, items[key], sep=' : ')
