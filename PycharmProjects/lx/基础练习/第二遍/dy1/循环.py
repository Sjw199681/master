a = 0  # 循环变量
while a < 5:  # 循环判断
    print("1")  # 循环体
    a += 1  # 循环变量发生变化
print("222")

# 累加偶数变量
result = 0
i = 1
while i<=100:
    if i %2==0:
        result +=i  # 判断条件--余数=0是偶数 余数=1是基数
    i+=1
print(result)


# # break--结束整个循环
# i=1
# while i<=10:
#     if i==5:
#         print("结束当前循环")
#         break
#     print(i)
#     i+=1



# continue--结束当前循环
i=1
while i<=10:
    if i>8:
        print("结束当前循环")
        i+=1
        continue
    i+=1
    print(i)

# for循环
a = '123456'
for i in a:
    if i=="1":
        print("不需要打印")
        continue
else:
    print("需要打印")


# range控制循环次数
# 九九乘法表
a=1
for a in range(1,10):
    for i in range(a,10):
        print("%d*%d=%d"%(a,i,a*i),end= "\t")
    i+=1
    print()
a+=1


# 打印正方形
a=5
for a in range(0,5):
    for i in range(0,5):
        print("*",end="")
    print()
    i-=1
a-=1