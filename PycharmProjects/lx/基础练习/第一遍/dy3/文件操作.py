# 建立一个文件
# f = open("text.txt", "w", encoding="utf-8")
f = open("text1.txt", "r+")  # r+在最开头但是会覆盖第一个   a+在最后加入   w+会清空后加入
f.write("""I have a dream
# I say to you, my friends, so even though we must face the difficulties of today and tomorrow, I still have a dream. It is a dream deeply rooted in the American dream.
# I have a dream that one day this nation will rise up and live out the true meaning of its creed - we hold these truths to be self-evident, that all men are created equal.
# I have a dream that one day on the red hills of Georgia, sons of former slaves and sons of former slave-owners will be able to sit down together at the table of brotherhood.
# I have a dream that one day, even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice.
# I have a dream my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.
# I have a dream today!
# I have a dream that one day down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification, one day right there in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers.
# I have a dream today.
# I have a dream that one day every valley shall be exalted, every hill and mountain shall be made low, the rough places shall be made plain, and the crooked places shall be made straight and the glory of the Lord will be revealed and all flesh shall see it together.
# This is our hope. This is the faith that I go back to the South with.
# With this faith we will be able to hew out of the mountain of despair a stone of hope.
# With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood.
# With this faith we will be able to work together, to pray together, to go to jail together, knowing that we will be free one day.
# This will be the day when all of God's children will be able to sing with new meaning-"my country 'tis of thee""")


# 关闭文件并保存
# n = f.read(10)  # 读取指定长度的文件
n=f.readline()#一次性读取，按照列表展示出来
list1={n}
print(list1)
for i in range(5):
    n=f.readline()#读取一行数据,一次读取一行
    print(n)
    list1.append(n)
    i+=1
print(list1)
b=f.seek(0,1)#打印当前指针位置 0 文件开头，1当前位置，2文件结尾
c=f.tell()#当前指针在哪里
print(n)
print(c)
# #关闭文件
f.close()

import os

# 文件读写
# 1.文件重命名
os.rename("text.txt","text1.txt")
# 2.删除文件
os.remove("text.txt")
# 3.创建文件夹
import time
#
os.mkdir("text2.txt")
time.sleep(3)
# 4.删除文件夹
os.rmdir("text2.txt")

# 5.获取当前目录
print(os.getcwd())

# 6.改变默认目录
os.chdir("/Users/songjianwei/PycharmProjects/untitled1")
print(os.getcwd())
# 7.获取目录列表
print(os.listdir("/Users/songjianwei/PycharmProjects/untitled1"))
# 8.获取当前的Py文件的目录
print(os.path.dirname(__file__))
