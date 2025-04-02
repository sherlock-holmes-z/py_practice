# object是基类，可以不写，默认继承
class Person(object):
    pass


tom = Person()
print(type(tom))
print(isinstance(tom, object))
print(isinstance(tom, Person))
