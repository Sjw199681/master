
try:
    open('text.txt','r')
except:
    print("出现异常，直接创建")
    # 创建某个文件
    open('text.txt','w')


#制定捕获某个指定异常
try:
    print('a')
except NameError:
    print("捕获指定异常")

# 捕获所有异常
try:
    print("1")
except Exception as res: # Exception捕获所有异常
    print(res)
else:
    print("没有捕获异常进行触发")  # else是except没有捕获错误执行的代码
#无论是否出现异常都执行
finally:
    print("不管有没有捕获报错都执行")



# 抛出捕获到的异常--抛出上一步的
try:
    print("1")
except Exception as rag:
    rag1 = "name 'n' is not defined"
    rag2=str(rag)
    if rag2 == rag1:
        print(rag)
    else:
        print(f"外部异常{rag}")
    raise


# #手动抛出指定异常
raise NameError