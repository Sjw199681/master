list2 = []
for i in range(1, 11):
    list2.append(i)
print(list2)

# 推导式---固定写法--必须这么写
# 生成一个列表
list2 = [i for i in range(1, 11)]
print(list2)
# 创建0-10的偶数列列表
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

# 字典推导式

# 创建⼀个字典:字典key是1-5数字，value是这个数字的2次⽅
a = {i: i for i in range(10) if i % 2 == 0}
print(a)

# 将两个列表合并为⼀个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
list3 = {list1[i]: list2[i] for i in range(len(list1))}
print(list3)

# 提取字典中⽬目标数据--提取上述电脑数量大于等于200的字典数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
list4 = {k: v for k, v in counts.items() if v >= 200}
print(list4)

#集合推导式
#创建⼀个集合，数据为下⽅列表的2次⽅
s2 = [1,3,4,5,6,7]
s1={i**2  for i in s2}
print(s1)