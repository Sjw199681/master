'4、求斐波那契数列 1 1 2 3 5 8 13 ……''重要==============='
str1 = 1
str2 = 1
list1 = []
for i in range(10):
    str3 = str1 + str2  # 第三个数=第一个数和第二个数相加
    list1.append(str1)
    # 第四个数=第二数+第三个数
    str1 = str2
    str2 = str3
print(list1)