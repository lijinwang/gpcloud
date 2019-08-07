#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: dict opera


ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}

# 取字典中键对应的值
print(ips['1.1.1.1'])

# 取字典中的键(唯一的),
for keys in ips.keys():
    print(keys)

# 取字典中的值(不唯一),
for values in ips.values():
    print(values)

# 取字典中的键值对
for item in ips.items():
    print(item)


