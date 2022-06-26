list1 = ["Tom", "Lixiang", "sjw", "sjw", "sjw"]
# 列表取值
print(list1[1])
# 查找--index 只会查找到第一个
print(list1.index("sjw"))
# 查找出现次数--count 不支持设置取值范围
print(list1.count("sjw"))
# 查看列表长度，元素个数--len
print(len(list1))
# 查看列表是否在取值范围内--in not in
print('sjw' in list1)
print('sjw' not in list1)
# 增加--append
a="lwh"
list1.append(a)
print(list1)
# 追加一个序列
# 1---加入的是一个列表
list1.append(['llll','ssss'])
print(list1)
# 2-追加序列内每个元素到列表--extend

list1 += ["hak", "cad"]  # 两种实现方式
print(list1)
list1.extend("ssssssss")  # "ssssss"相当于一个列表，都加入了进去
print(list1)
# 追加元素到指定位置---insert -占了指定位置的数据的位置，其余向后退一位
list1.insert(1,'追加元素到指定位置')
print(list1)
# 删除--del
# del list1
# 删除指定位置数据
# del  list1[1]
# pop() 删除指定下标的数据(默认为最后⼀一个)，并返回该数据,
print(list1.pop(0))
# remove() 移除列列表中某个数据的第⼀一个匹配项
list1.remove("追加元素到指定位置")
print(list1)
# clear():清空列列表
list1.clear()
print(list1)

list2 = ['Tom', 'Lily', 'Rose']
# 修改指定下标数据
list2[1]="这是一个修改数据"
print(list2)


#逆置:reverse() ---直接逆置
list2.reverse()
print(list2)

# #reversed()--不直接逆置
reversed(list2)
print(list2)

# #循环
# name_list = ["Tom", "Lixiang", "Sjw", "Sjw", "Sjw"]
#
# a = 1
# while a < len(name_list):
#     print(name_list[a])  # ---循环取值
#     a += 1
#
# for i in name_list:
#     print(i)
