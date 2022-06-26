# 3.三角形
# 打印三角形---倒三角
# a=5
# while a>0:
#     i=a
#     while i>0:
#         print("*",end="")
#         i-=1
#     a-=1
#     print()
# 正三角
# a=1
# while a<=5:
#     i=1
#     while i<=a:
#         print("*",end="")
#         i+=1
#     a+=1
#     print()


# 3.三角形的不同样子（右对齐，正三角形）
# 三角形-正三角形 center函数
a = 1
while a <= 10:
    i = a
    while i <= a:
        b = ("* " * i)
        print(b.center(20, " "), end=' ')
        i += 1
    a += 1
    print()
# 三角形
a = 1
while a <= 5:
    i = 1
    str1 = " "
    while i <= a:
        str1 += ("* ")
        i = i + 1
    print(str1, end='')
    a += 1
    print()

# 右对齐--rjust
a = 1
while a <= 5:
    i = a
    while i <= a:
        b = ("* " * i)
        print(b.rjust(10, ' '), end='')
        i += 1
    a += 1
    print()
