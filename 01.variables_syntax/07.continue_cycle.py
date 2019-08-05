#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: jump cycle continue


# for i in range(1, 101):
#     if i % 2 == 0:
#         continue
#     print(i)


for i in range(1, 101):
    for j in range(1, 101):
        if j % 2 == 0:
            continue
        print(j)
    print("i = ", i)
