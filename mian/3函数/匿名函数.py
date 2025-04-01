# 普通函数
def f1(a,b):
    return a+b
print(f1(1,2))

# 匿名函数
f2 = lambda a,b:a+b
print(f2(1,2))


list1 = [1,2,3]
for i in range(len(list1)):
    list1[i] = list1[i]**2
print(list1)

# 匿名函数一般在map中使用，
# map会对参数中的每个元素遍历执行函数操作
r = map(lambda x: x**2, list1) # 映射
print(list(r))

from functools import reduce
# reduce  对参数中的每个元素执行累加函数操作
r = reduce(lambda x,y:x+y,list1)
print(r)
r = reduce(lambda x,y:x*y,list1) # 累乘
print(r)

# filter，对参数中的元素进行过滤，只留下返回true的元素
r = filter(lambda x: x % 2 == 0, list1)
print(list(r))

r = reduce(lambda x,y:str(x) + str(y),list1)
print(r,type(r))
