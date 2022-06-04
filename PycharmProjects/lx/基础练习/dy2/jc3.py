'3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  #不允许用强制类型转化'
list1 = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
list2 = []
for i in range(len(list1)):  # 循环把list1按照底标里面的取出来
    # print(list1[i])
    if list1[i] not in list2:  # 判断l1的不能在l2里
        list2.append(list1[i])  # 把取出来的增加进去
print(list2)