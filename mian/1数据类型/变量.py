# 同时定义多个相同变量
num1 = num2 = num3 = 10.0
print(num1, num2, num3)
print("num1* num2 = %.3f" % (num1 * num2))

# 判断变量类型
print(isinstance(num1,float))

# 同时定义多个不同变量
str1,str2 = 234,"123"
print(type(str1),type(str2))

# py没有专门的常量类型，一般约定俗成大写的变量为常量
PI = 3.14
print(PI)

