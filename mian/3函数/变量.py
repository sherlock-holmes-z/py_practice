# 全局变量
num1 = 1
list1 = [1,2,3,4,5]

def f():
    num1 = 10 # 即使函数中定义num1，该num1也只在函数中生效，不会影响全局变量
    num2 = 10 # 函数内的是局部变量
f()
print(num1)


def f1():
    global num1 #使用global声明后，num1作为全局变量在函数中使用,用于不可变类型
    num1 = 20
    list1[0] = 0
    print(list1) # 可变类型不用global修饰
f1()
print(num1,list1)