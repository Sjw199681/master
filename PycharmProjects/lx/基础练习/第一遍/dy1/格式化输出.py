age = 18
name = 'Tom'
weight = 75.5
studen_id = 1

# 我的名字是TOM
print("我的名字是", name)

# 我的学号是0001
# % 06d   小技巧1
print("我的学号是%05d" % studen_id)

# 我的体重是75.5000000
print("我的体重是%f" % weight)

# 我的体重是75.50
# 技巧2     %.2f
print('我的体重是%.2f' % weight)

# 我的名字是TOM,今年18岁
print("我的名字是%s，我的年龄是%d"%(name, age))
# 我的名字是TOM,明年18岁
print("我的名字是%s，我明年年龄是%d"%(name, age + 1))

# # f表达式
# 我的名字是TOM,明年18岁
print(f"我的名字是{name},我明年是{age + 1}岁")

#方法-1：字符串前加r,字符串内容不会被转译
print(r"这是一个练习")
#方法2：字符串加\不会被转译
print("这是一 \n个练习")
#\t相当于tab按键
print('这是一 \t个练习')
#end=结尾的意思
print("这是一", end="")


#总结
"""%s:格式化输出字符串串
%d:格式化输出整数
%f:格式化输出浮点数
f-字符串串
f '{表达式}'
转义字符
\n:换⾏
\t:制表符 print结束符
"""






