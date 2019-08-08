#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: dict opera


ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
print(ips)

# 方式一: 使用冒泡排序进行字典中键值对排序
access = []
for item in ips.items():
    access.append(item)
print(access)
for i in range(len(access)):
    for j in range(len(access) - i - 1):
        if access[j][1] > access[j+1][1]:
            access[j], access[j+1] = access[j+1], access[j]
access = dict(access)
print(access, type(access))


# 方式二: 国盛法(针对字典的值排序)
listA, dictA = [], {}
for item in ips.items():
    listA.append(item[1])
listA.sort(reverse=True)
for values in listA:
    for item in ips.items():
        if values == item[1]:
            dictA[item[0]] = values
print(dictA)

