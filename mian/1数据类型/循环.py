num = 0
while num < 10:
    num += 1
    print(num)

print("*" * 10)

# range(10)生成0,1,2。。。。9的序列数字
for i in range(10):
    # if i == 5:
    #     continue
    # if i == 9:
    #     break
    print(i)

# 从2到9
for i in range(2,10):
    print(i)

print("*" * 10)

if num > 0:
    pass # 什么都不执行

print("*" * 10)
# for...else 循环没有被break时执行else，有break则不执行else
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print(1)

