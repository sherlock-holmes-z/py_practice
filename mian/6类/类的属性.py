class Person:
    def __init__(self):  # 初始化函数,构造函数
        print("init")


Person()


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age


gulu = Person2("zhangsan", 20)
print(gulu)
print(gulu.name, gulu.age)

# 可以修改属性值，添加新的属性值
gulu.age = 33
gulu.id = 1

# 获取所有属性，字典类型
print(gulu.__dict__, type(gulu.__dict__))
