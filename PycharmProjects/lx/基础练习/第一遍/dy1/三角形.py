# 3.三角形
# 打印三角形---倒三角
# a = int(input("打印列数： "))
# while a > 0:
#     list1 = a
#     while list1 > 0:
#         print("*", end="")
#         list1 -= 1
#     a -= 1
#     print()
# # 正三角
a = 1
while a <= 5:
    i = 1
    while i <= a:
        print("*", end='')
        i = i + 1
    a = a + 1
    print()



# 3.三角形的不同样子（右对齐，正三角形）
# 三角形-右对齐
a = 1
while a <= 10:
    i = a
    while i <= a:
        b = ("* " * i)
        print(b.center(20, " "), end='')
        i = i + 1
    a = a + 1
    print()

a=1
while a<=5:
    i = 1
    str1=" "
    while i <= a:
        str1 += ("* ")
        i = i + 1
    print(str1.center(20,' '), end='')
    a+=1
    print()





