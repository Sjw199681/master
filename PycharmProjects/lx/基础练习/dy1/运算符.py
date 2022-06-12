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



#总结
"""算数运算的优先级
混合运算优先级顺序:()⾼高于 ** ⾼高于 * / // % ⾼高于 + -
赋值运算符
=
复合赋值运算符
+=
-=
优先级
1. 先算复合赋值运算符右侧的表达式 2. 再算复合赋值运算的算数运算
3. 最后算赋值运算
⽐比较运算符
判断相等: == ⼤大于等于: >= ⼩小于等于:<= 不不等于: !=
逻辑运算符
与: and
或:or
非:not"""
