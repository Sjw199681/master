# 2.完成教程中未实现的作业:石头剪刀布
import random


#
# i=1
# while i<5:
#      a=random.randint(0,2)
#      b=int(input("石头剪刀布输入0/石头/1剪刀2/布："))
#      if b>2 or b<0:
#          print("输入错误重新输入")
#          continue
#      else:
#          if b==a:
#              print("平局")
#          elif b>a:
#              print("玩家胜利")
#              break
#          elif b<a:
#              print("电脑胜利")
#      i+=1
#
# else:
#     print("结束")


# 3.九九乘法表
# print('\n'.join(' '.join(["%2s x%2s=%2s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)))

# 打印正方形
# i=1
# while i <5:
#     n=0
#     while n<5:
#         print("*",end="")
#         n+=1
#     print('')
#     i+=1

# 打印三角形
# i=1
# while i <10:
#     print("*"*i)
#     i+=1
# 打印三角形
# # 循环变量
# h = 0


# 1、打印小猫爱吃鱼，小猫要喝水
class map:
    def chi(self, a):
        print(f"小猫爱吃{a}")

    def he(self, b):
        print(f"小猫爱喝{b}")


if __name__ == '__main__':
    pass


# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤

class Everyday:
    def __init__(self, name, weight):
        "name=姓名 weight=体重"
        self.name = name
        self.weight = int(weight)

    # 1）每次跑步会减肥0.5公斤
    def running(self):
        self.weight -= 0.5

    # 3）每次吃东西体重会增加1公斤
    def eat(self):
        self.weight += 1

    def __str__(self):
        return f"{self.name}现在的体重是{self.weight}"


if __name__ == '__main__':
    pass
    # a=Everyday("小明",75)
    # b=Everyday("小美",45)
    # a.running()
    # a.eat()
    # print(a)


# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
class FangZi:
    def __init__(self, hx, zmj):
        # 户型 - --外部传入
        self.hx = hx
        # 总面积 - --外部传入
        self.zmj = zmj
        # 家具列表
        self.list1 = []
        # 剩余面积 - -总面积 - 家具面积
        self.symj = self.zmj

    # 房子类的方法
    # 摆放家具
    def fangzi(self, meter):
        if meter.jjmj < self.zmj:
            # 能放下则追加到列表中
            self.list1.append(meter.name)
            self.symj -= meter.jjmj
        else:
            # 不能放下
            self.symj -= meter.jjmj
            print("放不下")

    def __str__(self):
        return f"户型是{self.hx}，总平米{self.zmj}，剩余平米{self.symj}，装的家具{self.list1}"


# 家具类
class Furniture():
    def __init__(self, name, jjmj):
        self.name = name
        self.jjmj = jjmj

    def __str__(self):
        return f"家具是{self.name},面积占用{self.jjmj}"


if __name__ == '__main__':
    # a=Furniture("床",4)
    # a1=Furniture("大炮",99)
    # b=FangZi('两居室',100)
    # b.fangzi(a1)
    # print(b)
    pass


# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

# 士兵类
# 枪名字--外部传入
# 装子弹 初始0
# 射击   子弹>0
class ShiBing:
    def __init__(self, name, sl, sjsl):
        self.name = name
        self.sl = sl
        self.sjsl = sjsl

    # 装子弹
    def zzd(self, sjsl):
        sjsl.jzd(self.sl)

    # 开枪
    def kaihuo(self, sjsl):
        sjsl.kaiqiang(self.sl)

    def __str__(self):
        return f"士兵{self.name},使用{self.sjsl}"


# 抢类
class Qiang:
    # 枪型号-外部传入(qxh)
    # 子弹数量 初始(zdsl)0
    def __init__(self, qxh):
        self.qxh = qxh
        self.zdsl = 0

    # 加子弹 子弹数量=sl
    def jzd(self, sl):
        if sl >= self.zdsl:
            self.zdsl += sl
            print(f"装填了{sl}子弹")
        elif 0 < sl < self.zdsl:
            self.zdsl += sl
            print(f"装填了{sl}子弹")
        elif sl < 0:
            print("最低装填1发")
        else:
            print("参数错误")

    # 开枪-外部传入开枪次数cs
    def kaiqiang(self, cs):
        if cs <= self.zdsl:
            self.zdsl -= cs
        elif cs > self.zdsl:
            print("子弹不足")

    def __str__(self):
        return f"枪型号{self.qxh}，剩余子弹数量{self.zdsl}"


if __name__ == '__main__':
    # a = Qiang("98k")
    # b = ShiBing("小名", 10, a)
    # a.jzd(100)
    # b.kaihuo(a)
    # print(b)
    pass

