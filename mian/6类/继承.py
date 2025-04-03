class Person:
    num = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.num += 1

    def say_hello(self):
        print("person hello")

class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)  # 调用父类构造方法
        self.clazz = clazz

    # 实例方法重写
    def say_hello(self):
        print("student hello")

class Teacher(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # 调用父类构造方法
        self.school = school


s1 = Student("zhangsan", 10, 1)
print(s1.__dict__, type(s1))
print(isinstance(s1, Person))
s1.say_hello()

t1 = Teacher("zhangsan", 10, "high school")
print(Person.num)
t1.say_hello()
