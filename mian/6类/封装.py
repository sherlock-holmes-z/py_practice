class Person:
    def __init__(self, name, age):
        self._name = name # 一个下划线表示受保护变量,不要轻易修改或使用
        self.__age = age # 两个表示私有变量

    def say(self):
        print(self._name + " is " + str(self.__age))

p1 = Person("zhangsan",19)
print(p1.__dict__)
# print(p1.__age) # 直接使用会报错
print(p1._Persion__age)
p1.say()