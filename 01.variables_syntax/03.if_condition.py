#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: if condition


# if 3 > 5:
#     print("3>5 is True")
# else:
#     print("3>5 is false")


# if 3 < 2:
#     print("你快拉倒吧你快拉倒吧")
# elif 3 < 4:
#     print("可以的")
# else:
#     print("这是废话")


variable = int(input("please input number: "))
if variable > 10:
    if variable < 20:
        print("variable is between of 10 to 20")
    else:
        if variable > 30:
            print("variable > 30")
        elif variable < 50:
            print("variable < 50")
else:
    if variable < 5:
        print("variable < 5")


