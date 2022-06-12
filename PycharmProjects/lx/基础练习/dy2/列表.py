name_list = ["Tom", "Lixiang", "Sjw", "Sjw", "Sjw"]
# 列表取值
print(name_list[1])
# 查找
print(name_list.index("Sjw", 3, 5))  # 只会查找到第一个
# 查找出现次数
print(name_list.count("Sjw"))  # 不支持设置取值范围
# 查看列表长度，元素个数
print(len(name_list))
# 查看列表是否在取值范围内
print("Sjw" in name_list)
print("Sjw" not in name_list)

# 外部输入姓名进行查找
name = input("名字: ")
if name in name_list:
    print("有名字", name_list.index("Sjw", 3, 4))
else:
    print("没找到")

name_list = ["Tom", "Lixiang", "Sjw", "Sjw", "Sjw"]
l = [1, 3, 4]
# 增加
name_list.append(l)
print(name_list)

# 追加一个序列
# 1---加入的是一个列表
name_list.append(["hal", "lao"])
print(name_list)
# 2-追加序列内每个元素到列表
name_list.extend(["hak", "cad"])
print(name_list)
name_list += ["hak", "cad"]  # 两种实现方式
print(name_list)
name_list.extend("ssssssss")  # "ssssss"相当于一个列表，都加入了进去
print(name_list)
# 追加元素到指定位置----占了指定位置的数据的位置，其余向后退一位
name_list.insert(3, "ppppp")
print(name_list)
# 删除
# del name_list
# print(name_list)
# 删除指定位置数据
del name_list[1]
print(name_list)
# pop() 删除指定下标的数据(默认为最后⼀一个)，并返回该数据
print(name_list.pop(1))  # 删除第二个位置的数据
# remove() 移除列列表中某个数据的第⼀一个匹配项
name_list.remove("ppppp")
print(name_list)
# clear():清空列列表
name_list.clear()
print(name_list)

num_list = ['Tom', 'Lily', 'Rose']
# 修改指定下标数据
num_list[1] = "aaaa"
print(num_list)

# #逆置:reverse() ---直接逆置
num_list.reverse()
print(num_list)

# #reversed()--不直接逆置
reversed(num_list)
print(num_list)

# #循环
name_list = ["Tom", "Lixiang", "Sjw", "Sjw", "Sjw"]

a = 1
while a < len(name_list):
    print(name_list[a])  # ---循环取值
    a += 1

for i in name_list:
    print(i)
