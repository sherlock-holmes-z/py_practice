def func():
    print("func")


func()
print("*" * 20)


# 返回值为None
def func2(a, b):
    print("sum:", a + b)


func2(2, 3)
print("*" * 20)


def func3(a, b):
    return a + b


sum = func3(2, 3)
print(sum)
print("*" * 20)


# 默认参数,参数不输有默认值
def func4(name, age=10, sex='男'):
    return "我叫%s,今年%d,性别%s" % (name, age, sex)
print(func4("zhangSan"), func4("lisi", 10))

# 可变参数,可以有任意个
def total(*args):
    print(args) # 实际是个元组
    r = 0
    for arg in args:
        r += arg
    return r
print(total(1, 2, 3),total(4,5,6,7,8))

# 可变参数，接收字典
def total2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
user= {
    "name": "zhangsan",
    "age": 10
}
total2(**user)
