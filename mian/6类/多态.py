class Animal:
    def say(self):
        pass

class Dog(Animal):
    def say(self):
        print("wang")

class Cat(Animal):
    def say(self):
        print("miao")

def speak(animal:Animal):
    animal.say()

speak(Dog())


