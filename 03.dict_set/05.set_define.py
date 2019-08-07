#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: set opera


set01 = {1, 1, 1, 1}
print(set01, type(set01))

set02 = {1, 2, 3, 4, 5}
set03 = {4, 5, 6, 7, 8}

set04 = set02 | set03
print(set04)

set05 = set02 & set03
print(set05)

# search = int(input("please input: "))
# if search in set04:
#     print(True)
# else:
#     print(False)


set05.add("hello")
print(set05)
set05.add(7)
print(set05)

set05.update((1, 2, 3, 4))
print(set05)

set05.pop()
print(set05)
set05.pop()
print(set05)
set05.pop()
print(set05)

set05.remove("hello")
print(set05)

for element in set05:
    print(element)


list01 = [1, 2, 1, 2, 1, 3, 5, 3, 6]
list02 = list(set(list01))
print(list02)

