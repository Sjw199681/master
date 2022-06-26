'5、求100以内的质数（只能被1和它本身整除）''重要==============='

a = []
i = 2
for i in range(1, 101):
    b = 2
    for b in range(2, i):
        if i % b == 0:
            break
    else:
        a.append(i)
print(a)
