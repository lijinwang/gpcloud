#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: string


string01 = 'hello world'
print(string01)

string02 = "this's my house"
print(string02)

string03 = '''this's my house
your"s get out'''
print(string03)


# 格式化打印
# print("system monitor messages\n",
#       "\tCPU rate: ", "80%")
#        .......
warn = '''System monitor messages:
        CPU rate: {}
        MEM rate: {}
        DISK rate: {}
        NETWORK mbps: {}
    @{}'''.format("80%", "70%", "60%", "1000M", "yanzeren")
print(warn)


# 字符串支持索引、切片
string = "cloud1901,good,program"
print(len(string))

for index in range(len(string)):
    if "g" == string[index]:
        print("g is exits in string")

print(string[10:14])

slist = string.split(",")
for index in range(len(slist)):
    if "good" == slist[index]:
        print("good finded")

for element in slist:
    print(element)

# 字符串的替换
string = "hello world"
new_string = string.replace("o", "E", 3)
print(string)
print(new_string)

# 敏感词替换
search = input("please input your search: ")
if "苍老师" in search:
    print(search.replace("苍", "*"))
else:
    print(search)

