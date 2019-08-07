# 第一题: 反转句子
string = "thisismyhouse"
strlist = string.split()
strlist.reverse()
result = ""
for i in strlist:
    result += i + " "
print(result.rstrip())


# 第三题: 找出数字添加至列表
tuple01 = ("string", "world", 1, 2, 3, 4, 6, 9, 10)
result = []
for element in tuple01:
    if type(element) == int:
        result.append(element)
print(result)



# 第四题: 提取数字到字典中
list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
list02 = list01[0:3]
list02.extend(list(list01[3]))
list02.extend(list01[-1])
print(list02)


list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
result = []
for element in list01:
    if type(element) == tuple:
        for i in element:
            result.append(i)
    elif type(element) == list:
        for j in element:
            result.append(j)
    else:
        result.append(element)
print(result)


list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
list02 = list(list01[3])
list01.pop(3)
list02.extend(list01[-1])
list01.pop(-1)
list01.extend(list02)
print(list01)


list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
print(type(list01[3][:]))

list02=[]
list02.extend(list01[3][:])
print(list02)
# list02.extend(list01[0:3])
# list02.extend(list01[3][:])
# list02.extend(list01[4][:])
# print(list02)


# 第五题: 排序
list01 = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
for i in range(len(list01)):
    for j in range(len(list01) - i - 1):
        if list01[j] > list01[j+1]:
            list01[j], list01[j+1] = list01[j+1], list01[j]
print(list01)
