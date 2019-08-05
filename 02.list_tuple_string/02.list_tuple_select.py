#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: list and tuple


list01 = [123, 123.123, 3.14, "hello", "world", False]
tuple01 = (123, 3.14, 4.445, "hello", "kitty", True)

# 索引(0, 1, 2, 3, .....)
# [123, 123.123, 3.14, "hello", "world", False]
#   0       1     2       3        4       5
#   -6      -5    -4      -3       -2      -1
# 利用for循环把列表中的元素一一进行打印输出,遍历列表
for i in range(len(list01)):
    print(list01[i])

# 利用for循环把元组中的元素一一进行打印输出,遍历元组
for j in range(len(tuple01)):
    print(tuple01[j])

# 输出list01中所有的数字
for i in range(len(list01)):
    if type(list01[i]) == int or type(list01[i]) == float:
        print(list01[i])

# 切片slice
print(list01[3:5])
print(list01[3:])
print(list01[:5])
print(list01[-5:-1])
print(list01[1:-1])
print(list01[0:6])
print(list01[0:7])
print(list01[0:14])
# print(list01[14])


print("list01's {} is very good.".format(list01[1:-1]))
# print("list01's ", list01[1:-1], " is very good.")


print('''
the monitor messages:
    CPU: {}
    MEM: {}
    DISK: {}
'''.format("80%", "40%", "30%"))









