# 判断某人是否能上网，input输入的是str类型，但是需要int类型才能判断
age = int(input("请输入年龄："))

if age >= 18:
    print("开始上网")
else:
    print("不满18，不能上网")

# 多判断逻辑
age = eval(input("请输入年龄："))
if age <= 18 and age >= 0:
    print("童工")
elif age >= 19 and age <= 60:
    print("搬砖")
elif age > 61:
    print("颐养天年")
else:
    print("请正确输入")


money = eval(input("获取余额： "))
if money > 0:
    print("走着去")
    seat = int(input("获取座位数： "))
    if seat != 0:
        print("坐着去")
    else:
        print("没有座位，坐着去")
else:
    print("走着去")

