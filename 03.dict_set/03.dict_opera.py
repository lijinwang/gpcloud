#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: dict opera


ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
print(ips)

access = []
for item in ips.items():
    access.append(item)
for i in range(len(access)):
    for j in range(len(access) - i - 1):
        if access[j][1] > access[j+1][1]:
            access[j], access[j+1] = access[j+1], access[j]
access = dict(access)
print(access, type(access))
