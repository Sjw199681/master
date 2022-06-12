'8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转  #不允许用reverse'
a = "welocme to super&Test"
list1 = list(a)
for i in range(len(a)):
    list1[i], list1[-i - 1] = list1[-i - 1], list1[i]
print(''.join(list1))