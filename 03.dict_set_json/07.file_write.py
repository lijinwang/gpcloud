#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: file opera

# w是覆盖, a是追加
file = open(file="./txtFile/king.txt", mode="a", encoding='utf8')

# 覆盖操作(当如下方式增加内容是不是覆盖而是逐行增加)
file.write("hello world, hello kitty\n")
file.write("cloud1901 study python and cloud\n")
file.write("11223344\n")

# 一次性添加多行内容
file.writelines(('this\n', 'is\n', 'my\n', 'house\n'))

file.close()
