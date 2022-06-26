# 判断某人是否能上网，input输入的是str类型，但是需要int类型才能判断
# age = int(input("请输入年龄："))
# if age>=18:
#     print('可以上网')
# else:
#     print('年龄小于18不能上网')

# 多判断逻辑-打工人
# age = eval(input("请输入年龄："))
# if 18<=age<=60:
#     print("正常年龄，打工人")
# elif age>60:
#     print("打工人该退休了")
# elif age<18:
#     print("还是童工，过几年在打工吧")

#取钱
money = eval(input("获取余额： "))
if money>=1000:
    print("打车去")
elif 10<=money<1000:
    print("去做公交车")
    seat = int(input("获取公交车座位数： "))
    if seat>=1:
        print("有座位可以坐着去")
    else:
        print("公交车没座位，站着去")
elif money<10 and money>0:
    print("走着去")
else:
    print("没钱就在家呆着吧")

