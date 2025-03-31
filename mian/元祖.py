# tuple,与列表类似，但元祖的元素不能修改
tuple100 = (1, 1, 2, "3", False)
print(tuple100, type(tuple100))

tuple0 = (1,)  # 元组里只有一个元素时，后面要加逗号，
print(type(tuple0))

tuple0 = ()
print(type(tuple0))

tuple0 = tuple()
print(type(tuple0))

print(tuple100.count(1))
print(tuple100[3])

print(tuple100[::-1])

# 元素不止一种类型，无法判断大小会报错
# print(min(tuple),max(tuple))
print("*" * 20)

tuple1 = (1, 2, 3, 4)
print(len(tuple1), min(tuple1), max(tuple1))
print(tuple1 + tuple1)
print(tuple1 * 2)
print(1 in tuple1)

# 元组不能修改
# tuple1[0] = 0

tuple2 = (1, 2, 3, 4, 1)
print(tuple2.count(1))
print(tuple2.index(2))

# 元组中可以放元组
tuple3 = ((1, 2, 3, 4), (1, 2, 3, 4))
print(tuple3.count((1, 2, 3, 4)))

print("tuple遍历" + "*" * 10)
for item in tuple3:
    print(item)

for i, item in enumerate(tuple3):
    print(i, item)

for i in range(len(tuple3)):
    print(i, tuple3[i])

print("类型转换" + "*" * 20)
tuple4 = tuple(range(10))
print(tuple4)
list1 = list(tuple4)
print(list1)
str1 = str(tuple4)
print(str1, type(str1))
tuple4 = tuple("abc")
print(tuple4)
