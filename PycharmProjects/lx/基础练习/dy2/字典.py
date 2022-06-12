# 字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男', '20000': '30'}
# 查询key---有则替换
dict1['name'] = "汤姆"
print(dict1)
dict1['Country'] = "英国"  # 查询key---无则增加
print(dict1)
# 删除--某个参数--key--删除整个健值对
del dict1['Countruy']
print(dict1)
del dict1  #删除字典
# 清空
dict1.clear()
print(dict1)
# 查询--根据key查询---找到返回找到的对应值，找不到返回默认值(None)或者写的默认值
print(dict1.get("200", "默认值"))
# 查询整个key
print(dict1.keys())
# 查询整个value
print(dict1.values())
# items----查询所有
print(dict1.items())

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男', '20000': '30'}
# 遍历字典的key
for i in dict1:
    print(i)

# 遍历字典的value
for i in dict1.values():
    print(i)

# 遍历字典的所有元素
for i in dict1.items():
    print(i)

# 遍历字典的键值对
for key, values in dict1.items():
    print(f"{key}={values}")
