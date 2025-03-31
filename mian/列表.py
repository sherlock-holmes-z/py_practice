
list1 = []

# 列表中的元素类型可以不一样
list2 = [1,2,"qwe",True]

list3 = list()

list4 = list("abcdefghijk") # 类型转换，str会拆分后作为列表。整数和布尔类型不可以转换，会报错

print(list1,list2,list3,list4)
print(type(list1),type(list2),type(list3))
print("*" * 10)

# 列表索引,不能超过索引范围
print(list2[1],list2[-1])
print(list4[2:4],list4[2:10:2])

# 列表的加法
print(list2 + list4)

# 列表乘法
print(list2 * 2)

print(1 in list2, 3 not in list2)
print(1 in ["1","2"])

# 内置函数  函数名(变量)
print(len(list4),max(list4),min(list4))

# 从内存中删除，再使用会报错
del list1
# print(list1) # 会报错

# 列表遍历
for i in list4:
    print(i)

print("*" * 10)

# 打印索引及元素
for i,j in enumerate(list4):
    print(i,j)
# 等同于
for i in range(len(list4)):
    print(i,list4[i])

print("*" * 10)

# 方法 变量.方法名()
list5 = list("12345")
list5.append("6")
print(list5)
list5.extend([7,8]) # extend加的是列表,相当于+
print(list5)

list6 = [1,2,3,4,5,6,7,8,9]
print(sum(list6) / len(list6))
