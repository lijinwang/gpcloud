#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: json format


import json


info = {
    'cpu': {
        'core': [2, 4, 8],
        'version': 'core i7',
        'price': 5000
    },
    'memory': {
        'size': [8, 16, 32],
        'HZ': '2133MHZ'
    },
    'disk': {
        'size': [500, 1000, 10000]
    }
}

with open(file='./txtFile/hardwareInfo.json', mode='w', encoding='utf8') as file:
    file.write(json.dumps(info))

with open(file='./txtFile/hardwareInfo.json', mode='r', encoding='utf8') as file:
    content = file.read()
    print(content, type(content))
    dictA = json.loads(content, encoding='utf8')
    print(dictA, type(dictA))

