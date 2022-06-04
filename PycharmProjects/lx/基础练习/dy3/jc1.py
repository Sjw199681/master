# 1.使用列表推导式生成能被5整除的数（100以内）

list1 = [i for i in range(100) if i % 5 == 0]
print(list1)





# 2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
#推倒式
list1 = ['小明', '小强', '小和', '小肖']
list2 = [222, 19, 18, 17]
list3 = {list1[i]: list2[i] for i in range(len(list1))}
print(list3)
