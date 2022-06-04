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
    a = Qiang("98k")
    b = ShiBing("小名", 10, a)
    a.jzd(100)
    b.kaihuo(a)
    print(b)

