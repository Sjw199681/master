# 2.完成教程中未实现的作业:石头剪刀布
# 生成随机数
import random

i = 1
while i <= 100:
    suijishu = random.randint(0, 2)
    shuru = int(input("输入石头=0剪刀=1布=2：  "))
    if 0 < shuru > 2:
        print("参数不合法，重新输入")
        continue
    else:
        if shuru > suijishu:
            print("玩家胜出,结束")
            break
        elif shuru < suijishu:
            print("电脑胜出，继续")
            continue
        elif shuru == suijishu:
            print("平局")
            continue
