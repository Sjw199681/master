# 3.开发一个注册系统，
# 页面：
# [{name:xxx,age:xxx},{name:xxx,age:xxx},{name:xxx,age:xxx}]
# ----------------
# *   1-新增用户
# *   2-查询用户
# *   3-删除用户
# ----------------
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
# 功能2：查询学生信息
# 功能3：删除学生信息


# 存储库
memory = [{'name': "小明", 'age': 20, 'gender': '男'}, {'name': "小强", 'age': 21, 'gender': '女'},
          {'name': "小亮", 'age': 22, 'gender': '男'}]


# 新增-查找
def chaozhao(name):
    for i in range(len(memory)):
        if name == memory[i]["name"]:
            return f"{name}有相同的学生信息"


# 功能1：新增学生信息
def xinzeng(name, age, gender):
    chaozhao(name)
    name1 = f"{name}有相同的学生信息"
    if name1 == name:
        print(f"{name}有相同的学生信息,不能添加")
    else:
        memory.append({"name": name, "age": age, "gender": gender})
        print(f"{name}学生信息加入成功")


# 功能2：查询学生信息
def chaxun(name):
    for i in range(len(memory)):
        if name == memory[i]["name"]:
            print(f"{name}有相同的学生信息")
            break
        else:
            print(f"学生{name}信息不存在")


# 功能3：删除学生信息
def shanchu(name):
    for i in range(len(memory)):
        if name == memory[i]["name"]:
            del memory[i]
            print(f"成功删除{name}学生信息")


def run():
    while True:
        print("--------------------------------")
        print("请选择使用的功能\n1=新增学生信息\n2=查询学生信息\n3=删除学生信息\n4-退出")
        a = (input("请输入选项： "))
        print("--------------------------------")
        if a == "1":
            print("新增学生信息")
            name = (input("学生姓名："))
            age = int(input("学生年龄："))
            gender = (input("学生性别："))
            if gender == "男" or gender == "女":
                print("输入正常")
            else:
                print("只能输入男/女")
                break
        elif a == "2":
            print("查询学生信息")
            name = input("学生姓名：")
            chaxun(name)
        elif a == "3":
            print("删除学生信息")
            name = input("删除的学生姓名：")
            shanchu(name)
        elif a == "4":
            break
        else:
            print("参数不合法")
            break


run()
