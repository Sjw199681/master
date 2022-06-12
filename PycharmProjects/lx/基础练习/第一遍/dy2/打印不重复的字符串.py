'6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef'
a = "aabbbcddef"
b = ""
for i in a:  # 循环把元素取出来
    if a.count(i) <= 1:  # 对比总数不大于1的
        b = b + i
print(b)