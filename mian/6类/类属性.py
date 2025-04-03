class Person:
    num = 0  # 类属性，相当于java的静态变量

    def __init__(self, name):
        self.name = name
        Person.num += 1
        print("init")


p1 = Person("lisi")
print(p1.__dict__,Person.num)

p2 = Person("wangwu")
print(Person.num)
