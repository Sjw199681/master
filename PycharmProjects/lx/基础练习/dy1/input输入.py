# 输入密码
# password = input("输入密码：")
#
# print(password)
# # input把所有接受到的信息存储成字符串类型
# print(type(password))

str1 = "22222"
str2 = "[1,2,3,4,5]"
str3="(1,2,3,4,5)"
str4="2.345"
#转换成eval类型----转换成最相近的类型
data1 = eval(str2)
print(data1)
#转换成int类型---整数类型
data2 = int(str1)
print(data2)
#转换成float类型---浮点类型
data3= float(str4)
print(data3)
#转换成str类型---字符串类似
data4=str(str3)
print(data4)
#转换成list类型---列表类型
data5=list(str1)
print(data5)
#tuple 转换成一个元组
data6=tuple(str1)
print(data6)



# 总结
# 转换数据类型常⽤用的函数
# int()
# float()
# str()
# list()
# tuple()
# eval()
