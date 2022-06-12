# 2.完成教程中未实现的作业:石头剪刀布
# 生成随机数
import random

i = 1
while i <= 100:
    computer = random.randint(0, 2)
    player = int(input("请输入石头/0剪刀/1布/2:  "))
    if player > 2 or player < 0:
        print("输入不合规")
        continue
    else:
        if player > computer:
            print("玩家胜利")
            break
        elif player == computer:
            print("平局")
            i += 1
        elif player < computer:
            print("电脑胜利")
            i += 1
else:
    print("玩家胜利")


if __name__ == '__main__':
    pass

