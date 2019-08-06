#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: list and tuple


list01 = [1, 3.14, 1, False, "String Type"]

number = list01.count(0)
print(number)

index = list01.index(1, 1, 4)
print(index)

# 在列表中最后一个位置进行元素的追加
list01.append("hello world")
print(list01)

# 在列表任意一个位置进行元素的插入
list01.insert(0, "insert")
print(list01)

# 将另外的列表拓展到当前列表中
list02 = [1, 2, 3, 4, 5]
list01.extend(list02)
print(list01)

# 列表最终还是存在的, 在内存中还有相应的消费
# list01.clear()
# print(list01)

# 直接在内存中对列表进行移除
# del list01
# print(list01)

# 删除列表中的元素
list01.pop(4)
print(list01)

list01.remove("hello world")
print(list01)

# 排序
list01 = [23, 12, 41, 24, 46, 78, 20]
# list01.sort()
# print(list01)
#
# a, b = 1, 2
# a, b = b, a
# print(a, b)

# 冒泡排序
for i in range(len(list01)):
    for j in range(len(list01) - i - 1):
        if list01[j] > list01[j+1]:
            list01[j], list01[j+1] = list01[j+1], list01[j]
print(list01)

# 二分查找
list01 = [1, 2, 3, 4]
firstIndex, endIndex = 0, len(list01)-1
search = int(input("please input number: "))
while True:
    middleIndex = (firstIndex + endIndex) // 2
    if list01[middleIndex] > search:
        endIndex = middleIndex
    elif list01[middleIndex] < search:
        firstIndex = middleIndex
    else:
        print(middleIndex)
        break

# 反转列表
list03 = ["this", "is", "my", "house"]
list03.reverse()
print(list03)


