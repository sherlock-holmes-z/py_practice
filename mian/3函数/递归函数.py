def f(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 0:
        return 0
    else:
        return f(num - 1) + f(num - 2)
print(f(10))

list1 = [0,1,2]
for i in range(3,11):
    list1.append(list1[i-1] + list1[i-2]) # 列表的扩展只能用append方法
print(list1[len(list1)-1])