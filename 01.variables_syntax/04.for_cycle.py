#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: for cycle


# for i in range(101):
#     print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

for j in range(1, 101):
    if j % 2 == 1:
        print(j)

for k in range(1, 101):
    if k % 2 == 0 and k % 3 == 0:
        print(k)

