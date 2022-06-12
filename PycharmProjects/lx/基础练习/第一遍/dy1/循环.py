a = 0  # 循环变量

while a < 5:  # 循环判断
    print("111")  # 循环体
    a += 1  # 循环变量发生变化
print("222")

# 累加偶数变量
result = 0
i = 1
while i <= 100:
    if i % 2 == 0:  # 判断条件--余数=0是偶数 余数=1是基数
        result += i  #
    i += 1
print(result)

# # break--结束整个循环
i = 1
while i <= 5:
    if i == 3:
        print("包子坏了")
        break
    print(f"吃了{i}个包子")
    i += 1
print("吃饱了")

# continue--结束当前循环
i = 1
while i <= 6:
    if i == 3:
        print("包子坏了")
        i += 1  # 要加判断-要不会死循环
        # break
        continue
    print(f"吃了{i}个包子")
    i += 1
else:
    print("吃饱了")

# for循环
a = '123456'
for i in a:
    if i == '1':
        print("这个不打印")
        # break
        continue
else:
    print(i)

# range控制循环次数
# 九九乘法表
line=1
for line in range(1,10):
    for i in range(line,10):
        print("%d*%d=%d"%(line,i,line*i),end='\t')
        i =i+1
    print()
    line+=1
# 打印正方形
list1 = int(input("打印列数： "))
for i in range(0, list1):
    for a in range(0, list1):
        print("*", end="")
        a -= 1
    i -= 1
    print()