'1.需求：有三个办公室，8位老老师，8位老师随机分配到3个办公室'
import random

rooms = [[], [], []]  # 三个教室
teacher = [1, 2, 3, 4, 5, 6, 7, 8]  # 八位老师
for i in teacher:  # 循环老师
    dorm = random.randint(0, 2)  # 随机教室
    rooms[dorm].append(i)  # 把随机出的教室利用底标，追加对应的教室
print(rooms)
