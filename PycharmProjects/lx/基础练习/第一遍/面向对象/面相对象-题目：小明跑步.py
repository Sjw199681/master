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