# abs() 函数可以完成对数字求绝对值计算
print(abs(-10))
# round() 函数可以完成对数字的四舍五入计算
print(round(1.9))
# map()序列中各个数字的2次⽅
list1 = [1, 2, 3, 4, 5, 6]


def funs(x):
    return x ** 2


list2 = map(funs, list1)
print(list(list2))

# reduce()序列中各个数字的累加和
import functools

list1 = [1, 2, 3, 4, 5, 6]


def funs(a, b):
    return a + b


list2 = functools.reduce(funs, list1)
print(list2)

#filter()过滤掉不符合条件的元素

list1 = [1, 2, 3, 4, 5, 6]
