class Person:
    num = 0

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        Person.num += 1
        print("init")

    # 实例方法
    def say_name(self):
        print(self.__dict__)

    def level_up(self):
        self.level += 1

    # 类方法
    @classmethod
    def print_num(cls):
        print(cls.num)

    # 静态方法，可以用于实例的预处理判断，和类及实例本身没有任何关系
    @staticmethod
    def check(**kwargs):
        if kwargs['level'] > 100:
            return False
        else:
            return True


p1 = Person("lisi")
p1.say_name()
p1.level_up()
p1.say_name()

p2 = Person("wangwu")
Person.print_num()

if Person.check(**{"level": 200}):
    print(1)
else:
    print(2)
