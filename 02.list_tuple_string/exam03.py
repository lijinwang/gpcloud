# 第一题: 反转句子
# string = "thisismyhouse"
# strlist = string.split()
# strlist.reverse()
# result = ""
# for i in strlist:
#     result += i + " "
# print(result.rstrip())


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

