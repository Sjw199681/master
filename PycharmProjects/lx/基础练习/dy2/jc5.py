'5、求100以内的质数（只能被1和它本身整除）''重要==============='
list1 = []
i = 2
for i in range(2, 101):  # 循环100之内的所有数
    b = 2  # 因为1是和数也是质数所以从2开始
    for b in range(2, i):  # 循环2开始到i的数
        if i % b == 0:  # 余数=0则结束循环
            break
    else:
        list1.append(i)  # 余数不为0则追加
print(list1)