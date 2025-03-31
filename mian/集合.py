s = set()
print(s, type(s))

s = {1, 2, 3, 4, 1}
print(s)

s = set([1, 2, 3, 4, 1])  # list -> set
print(s, type(s))
s = set((1, 2, 3, 4, 2))  # tuple -> set
print(s, type(s))

s = set("112233")  # str -> set 1 2 3
print(s)

s = set({"name": 1, "age": 2})  # dict字典转set只留k
print(s)

# set中存放的字典必须是不可变的，dict是可变类型
# s = {
#     {"name": 1, "age": 2}, {"name": 2, "age": 3}
# }
# print(s)

print(1 in s)
print(len(s), min(s), max(s))

print("*" * 20)
for i in s:
    print(i)

s.add("abc")
print(s)

print("*" * 20)

# 交集，并集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2, s1.intersection(s2))
print(s1 | s2, s1.union(s2))

# 列表去重
score = [70, 80, 90, 70, 65, 78, 80, 90]
s = set(score)

d = {}
for i in s:
    d[i] = score.count(i)

for k, v in d.items():
    print("%d:%d" % (k, v))
