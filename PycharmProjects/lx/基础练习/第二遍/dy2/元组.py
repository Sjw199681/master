# 元组取值
tople1=(1,23,4,5,6,7,8998,1,1,2,2,1,1,1,1,1,1)
print(tople1[1])
# 根据元素查找元组中的下标，没有则报错--index
print(tople1.index(23))
# 统计次数--count
print(tople1.count(1))
# 统计元素个数--len
print(len(tople1))
# 元组中有列表 进行替换列表中的数据
tople2 = ('aaa', 'sss', 'ddd', [1, 2, 3, 4, 5, 5], 'fff', 'aaa', 11111)
tople2[3][2]="aaaaaaaa"
print(tople2)
print(tople2[6])  # 按照底标取元组中的值
# 取出列表
tople3 = tople2[4]
print(tople2[3])
