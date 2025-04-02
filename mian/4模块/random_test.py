import random

# 生成随机小数
r = random.random()
print(r)

# 1-10之间生成随机整数
r = random.randint(1, 10)
print(r)

# 获取列表中的随机元素
list1 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(list1[random.randint(0, len(list1) - 1)])

# 随机获取元素
print(random.choice(list1))

# 打乱元素
random.shuffle(list1)
print(list1)
