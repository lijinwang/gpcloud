#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: variable type


# int(整型)、float(浮点型)、str(字符串)、bool(布尔值)

var01 = 666
var02 = 6.6
var03 = "this's my house"
var04 = True

print(var01, type(var01))
print(var02, type(var02))
print(var03, type(var03))
print(var04, type(var04))

var05 = "123"
print(var05, type(var05))

var05 = int(var05)
print(var05, type(var05))

# var06 = "123.123"
# print(var06, type(var06))
#
# var06 = float(var06)
# print(var06, type(var06))

var05 = float(var05)
print(var05, type(var05))

var05 = int(var05)
print(var05, type(var05))

var05 = str(var05)
print(var05, type(var05))


readline = int(input("please input number: "))
print(readline, type(readline))
