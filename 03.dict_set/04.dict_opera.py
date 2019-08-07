#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: dict opera


ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
print(ips)

# 增加键值对
ips['19.19.19.19'] = 34
print(ips)

ips.setdefault('18.18.18.18')
print(ips)

ips.setdefault('13.13.13.13', 78)
print(ips)

ips.setdefault('192.168.161.10', 67)
print(ips)

ips.update([('17.17.17.17', 56), ('90.90.90.90', 78), ('12.12.12.12', 89)])
print(ips)

listA = ['192.168.161.10', '189.167.156.145', '10.10.10.10']
ipaddr = {}.fromkeys(listA)
print(ipaddr)

# 删除操作
ipaddr.pop('192.168.161.10')
print(ipaddr)

ipaddr.popitem()
print(ipaddr)

ipaddr.clear()
print(ipaddr)

# del ipaddr
# print(ipaddr)

# 修改操作
ipaddr = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
print(ipaddr)

ipaddr['192.168.161.10'] = 88
print(ipaddr)

ipaddr.update([('192.168.161.10', 100)])
print(ipaddr)


