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
    a=Furniture("床",4)
    a1=Furniture("大炮",99)
    b=FangZi('两居室',100)
    b.fangzi(a1)
    print(b)
