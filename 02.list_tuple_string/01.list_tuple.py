#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: list and tuple


tuple01 = (123, 123.123, "hello", False)
print(tuple01, type(tuple01))

list01 = [123, 123.123, "hello", False]
print(list01, type(list01))

# 查看list01和tuple01的大小
print("tuple01 size: ", tuple01.__sizeof__())
print("list01 size: ", list01.__sizeof__())

# 向列表中增加元素
tuple02 = tuple01 + ("world", )
list01.append("world")
print("tuple02 size: ", tuple02.__sizeof__())
print("list01 size: ", list01.__sizeof__())

list01.append("kitty")
print("list01 size: ", list01.__sizeof__())

list01.append("size")
print("list01 size: ", list01.__sizeof__())

list01.append("__sizeof__")
print("list01 size: ", list01.__sizeof__())

list01.append("sizeof")
print("list01 size: ", list01.__sizeof__())
