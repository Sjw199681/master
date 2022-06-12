# 索引
# 代码的取值是从0开始


# 切片
name = "0123456789"
# 重点----步长为负数的时候，取值的开始和结束要倒着写
print(name[4:1:-1])
# 从2开始取，到4结束---最后4舍去
print(name[2:4])
# 从开通取值到尾
print(name[0:])
# 最后取值3 是三步取一次
print(name[0::3])
# 步数是总2开始的
print(name[2:-1:2])
# 最后步数-1-----倒着取值如是-2则按照倒着两位取值
print(name[::-2])


# 查找.find()   .index()   统计 .count
mystr = "hello world and superctest and chaoge and Python"
print(mystr.find("and"))
# 加r是从右侧开始找
print(mystr.rfind("and"))
# index未找到则报错
print(mystr.index("and"))
# count=统计""总数
print(mystr.count("and", 0, 39))

# 修改---.replace
mystr = "hello world and superctest and chaoge and Python"
print(mystr.replace("and","he"))

# 分割，会把分割的字符吃掉(自动删除)--分割之后返回的是list格式
print(mystr.split("and"))

# 替换---.join()
list1 = ['hello world ', ' superctest ', ' chaoge ', ' Python']
str1 = "2".join(list1)
print(str1)


mystr = "   hello world and superctest and chaoge and Python   "
#转换--
#首字母变成大写
print(mystr.capitalize())
#每个首字母变大写
print(mystr.title())
#所有字母变小写
print(mystr.lower())
#所有字母变大写
print(mystr.upper())
#删除两侧空白字符
print(mystr.strip())

str1 = "*"
# # 补充字符串到指定长度--左添加
print(str1.ljust(10, "-"))
# # 补充字符串到指定长度--右添加
print(str1.rjust(10, " "))
# 补充字符串到指定长度--居中
# 只能补充一个字符串，不能补充多个
print(str1.center(9, " "))


mystr = "   hello world and superctest and chaoge and Python   "
print(mystr.endswith('hello'))