import math
from decimal import Decimal, getcontext

num1, num2 = 11.123, 2.2345
print(num1 + num2) # 直接相加运算结果不精确

print(round(num1+num2,2)) # 保留两位小数，四舍五入

print(math.ceil(num1 + num2)) # math库，向上取整
print(math.floor(num1 + num2)) # math库，向下取整

# 精确计算
getcontext().prec = 10 # 最终结果保留几位数字
a = Decimal('11.1234')
b = Decimal('23.34567')
print(a + b)

# None,0, 0.0 ,空容器都可以解释为false
print(type(None))

# 空串,变量不能命名为str，否则会覆盖str()函数
str1 = str()
print(type(str1))
print('结果 %s ' % (str1))

str1 = "字符串"
print(str1 * 3)
num = 3
str1 = str1 + str(num)
print(str1)
# print(str + 3) # 字符串和数字不能相加

str1 = "包含\'\"的字符串\""
print(str1)

str1 = "helloworld"
print(str1[0:5:2]) # 0-5,+2取值，即间隔1位取值
print(str1[::2]) # 整个字符串从0开始，间隔1位取值
print(str1[-1])
print(str1[1:3]) # 左闭右开

numStr = "123456789"
print(numStr[-1:-10:-1]) # 字符串反转
print(numStr[::-1])

# true为1，false为0
print(int(True))
print(int(False))

s1 = "123"
print(bool(s1),bool("")) # bool判断真假，字符串只要有值就为true
print(bool(0),bool(123)) # 数字只要非0就为true

num1 = 1
num2 = 1
print(id(num1),id(num2)) # -5到256之间的整数共用一个地址
