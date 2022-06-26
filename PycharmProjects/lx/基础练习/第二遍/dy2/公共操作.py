# 运算符  +(列表，元组，字符串)
# str1="1,3,4,5"
# str2="2323"
str1 = [1, 3, 4, 5]
str2 = [2, 3, 4, 5]
print(str1 + str2)

#    *(列表，元组，字符串)
str3 = "&&&&&&&&"
print(str1 * 1)
print(str3 * 4)

# in或not in(列表，元组，字符串)
print("a" in str1)
print(1 in str1)
print(1 not in str2)

# 公共方法
# 1.len()计算容器器中元素个数--长度(字符串,列表，元组，集合，字典)
str4 = "2,3,4,5,6,7,7"
str5 = [1, 3, 4, 5, 6, 7]
str6 = {1, 2, 3, 4, 5, 6, 7, 8, 8, 0}
print(len(str6))

# del 或 del()删除(字符串，列表)
list1 = [1, 23, 4, 5, 6, 7]
del list1[1]  # 删除列表某个位置的数值
print(list1)
list2 = "1232323"  # 字符串只能全部删除
del list2

# max() 返回容器器中元素最大值(字符串，列表)
max1 = 1, 3, 4, 4, 5, 56, 7
max2 = [10, 20, 30, 40]
print(max(max1))
print(max(max2))

# min() 返回容器器中元素最小值(字符串，列表)
min1 = 1, 3, 4, 4, 5, 56, 7
min2 = [10, 20, 30, 40]
print(min(min1))
print(min(min2))

# range()--随机数
for i in range(1, 10, 2):  # 生成从start到end的数字，步长为 step，供for循环使⽤
    print(i)

# enumerate()
# 枚举-函数用于将⼀个可遍历的数据对象(如列表、元组或字符串)组合为⼀个索引序，同时列出数据和数据下标，一般⽤在 for 循环当中
list1 = [1, 2, 3, 4, 5, 6, 7]
for i in enumerate(list1, start=7):
    print(i)
for a, b in enumerate(list1, start=9):
    print(f"这是{a}这是{b}")

# 容器转换
#tuple()  转换成元组
list3=[1,23,4,5,6]
list4={1,23,3,4,5,6,7,}
print(tuple(list1))

#list() 转换成列表---整数不能转换
list1=123455677
list2="1234566"
print(list(list2))

#set()  转换成集合
print(set(list2))
