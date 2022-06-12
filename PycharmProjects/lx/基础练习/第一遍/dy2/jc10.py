'10、有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set'
# 取出值，判断元素是否在列表中，是否总数大于1 不在则追加
str1 = "aabbbcddef"
list1 = []
# for i in range(len(str1)):
#     c = str1[i]
#     if c not in list1:  # 判断取出来的没在列表里
#         if str1.count(str1[i]) < 1:  # 如果取出来的总数小于1则结束，大于1则追加
#             continue
#         else:
#             list1.append(str1[i])
# list2 = "".join(list1)
# print(list2)


for i in str1:
    if i not in list1:
        list1.append(i)
print("" .join(list1))

