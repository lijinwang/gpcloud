#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: file opera


file = open(file="./txtFile/kingdoms.txt", mode="r", encoding="utf8")

# 读取全文
# content = file.read()
# print(content)

# 读取文件中的行
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)

# 读取文章中所有的行,把各个行作为列表中的元素
# content = file.readlines()
# print(content)

file.close()
