# 值可以是任何数据类型，key必须是字符串，数字，元组
dict1 = {}
print(dict1, type(dict1))
dict1 = dict()
print(dict1, type(dict1))
dict1 = {1: 1, "name": "张三", ("a", "b"): ("c", "d")}
print(dict1, type(dict1))

# 相同属性不会报错，但会被覆盖
dict2 = {
    "name": "张三",
    "age": 10,
    "name": "李四"
}
print(dict2, type(dict2))

# 新增属性
dict2["sex"] = "男"
print(dict2)

# 获取属性值
print(dict2["name"], dict2.get("name"))

# 修改v
dict2["name"] = "lisi"
print(dict2)

# 只能判断key，不能判断value
print("name" in dict2, "lisi" in dict2)

# 遍历
for i in dict2:
    print(i, dict2[i])

for k, v in dict2.items():
    print(k, v)

# 只遍历k
for k in dict2.keys():
    print(k)
# 只遍历v
for v in dict2.values():
    print(v)

print("常用方法：" + "*" * 20)
# 删除元素
print(dict2.pop("name"), dict2)
a = dict2.copy()
dict2["name"] = "wanguw"
print(a, dict2)

dict2.popitem()  # 删除末尾的kv
print(dict2)

# 更新元素,有就更新，没有新增
dict2.update({"sex": "nv", "food": "apple"})
print(dict2)
dict2.clear()
