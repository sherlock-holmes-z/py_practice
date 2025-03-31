year = 2025
month = 3
day = 29
weekday = '四'
print(year,"hello world",sep='年 ',end='\n\n')
print('------------')

# %d占位符
print("today is %d年%d月%d" % (year,month,day))

# %d 数字占位符 %02占两位，不够用0补充
print("today is %d年%02d月%d" % (year,month,day))

# %s 字符串占位符
print("today is 星期%s" % (weekday))

# %f 浮点数占位符 .2保留两位小数
num = 1.2
print("num is %.2f" % (num))


# 默认输入都是str类型
a = input("please enter:")
print(type(a))
print(a)

b = input("please enter:")
b = int(b)
print(type(b))
print("%d" % (b))