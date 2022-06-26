age = 18
name = '啦啦啦'
weight = 75.5000000
studen_id = 100

# 我的名字是TOM
print("我的名字是",name)
# 我的学号是0001
# % 06d   小技巧1
print("我的学号是%d"%studen_id)
# 我的体重是75.5000000
print("我的体重是",weight)
# 我的体重是75.50
# 技巧2     %.2f
print("我的体重是%.2f"%weight)
# 我的名字是xx,今年18岁
print("我叫%s,今年%d岁"%(name,age))
# 我的名字是xx,明年19岁
print("我叫%s,明年%d岁"%(name,age+1))
# # f表达式
# 我的名字是xx,明年18岁
print(f"我叫{name},今年{age}岁")
#方法-1：字符串前加r,字符串内容不会被转译
print(r"lalalalalla")
#方法2：字符串加\n不会被转译
print("llalalalala\nlalalallalala")
#\t相当于tab按键
print("lalallalal\n这是第二段lalalalla")
#end=结尾的意思
print("lallalalal",end="这是一个结尾")


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






