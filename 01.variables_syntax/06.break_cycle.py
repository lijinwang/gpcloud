#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: jump cycle out


for i in range(100):
    print(i) # - 23
    if i == 23:
        break


while True:
    variable = input("please input your word: ")
    if variable == "bavdu":
        break
