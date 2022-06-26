# 多个变量量赋值
str1, float1, int1 = '123', 2.1, 10
print(str1)
print(float1)
print(int1)

# 多变量量赋相同值
a = b = c = 10
print(c)



#复合赋值运算符
c = 10
c += 1 + 2
# 输出13, 先算运算符右侧1+2=3， c+=3, 推导出c=10+3 print(c)

b=2
b *= 3
print(b)
# 输出6 b=b*3,最终b=2*3 print(b)

#比较运算符
a=7
b=5
print(a == b) # False
print(a != b) # True
print(a < b) # False
print(a > b) # True
print(a <= b) # False
print(a >= b)# True

