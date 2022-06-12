# 函数进行1+2的计算--外界传进参数
# #函数定义
def add_ition(a, b):  # 形式参数
    """
    :param a   第一个数
    :param b   第二个数
    :return  add  a+b的求和
    """
    add = a + b
    return add


result = add_ition(10, 5)
help(add_ition)#查看函数的说明⽂档
print("计算:", result)


# 函数返回值
def return1():
    return "¥¥¥¥¥"

money = return1()
print("金钱的符号是：", money)

def print_line(n):
    while n>0:
        print("-------")
        n-=1

    # for i in range(n):
    #     print("-------")

print_line(5)

a=100

def text1():
    return a
def text2():
    global a
    a=10000
    print(a)
def text3():
    #修改全局变量
    global a
    a=10000000
    print(a)

text1()
text2()
text3()
# print(a)

def user_info(name, age, gender):
    print(f"姓名:{name},年龄:{age},性别:{gender}")

# 位置传参数
user_info("123", 23, "你猜猜")  # 位置传参数
#关键字传参数
user_info(age=23, gender="你猜我猜不猜", name="&0.123")  # 关键词传参
user_info("你猜猜",age=23,gender=222)


# 不定长传参  包裹位置传参
def user_info(*args):
    print(len(args))
    print(args)


user_info("123", "345", "789", "10",10000)
list1 = ["wwwwww", "ddddd", "ssss", "222"]
user_info(*list1)


# 不定长传参，包裹关键字传参---必须是个健值对的形式
def user_info1(**kwargs):
    print(kwargs)


# kwargs保存的是字典
user_info1(name="你猜", age=12, gender="男", 国家="中国")
dict1 = {"啦啦啦阿拉": "22222", "啦啦啦啦啦": "2222", "啦啦啦啦": "22222"}
user_info1(**dict1)


def name(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))


# name({"sssss",111})#集合不能拼接
name([1, 2, 3, 4, 5])  # 列表可以，拼接之后id一样
name((1, 2, 3, 4))  # 元组可以但是id不一样
name("字符串")  # 单个字符串可以，但是拼接之后id不一样
# name(1,2,3,4)#多个字符串不可操作
# name({"a":"b"})#字典不能拼接
