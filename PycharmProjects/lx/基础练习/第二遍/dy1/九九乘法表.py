# 九九乘法表
print('\n'.join(' '.join(['%dx%d=%d  '%( a, i,a * i)for a in range(1,i+1)])for i in range(1,10)))


a=1
while a<=9:
    i=1
    while i<=a:
        print("%d*%d=%d"%(i,a,a*i),end='\t')
        i+=1
    a+=1
    print()