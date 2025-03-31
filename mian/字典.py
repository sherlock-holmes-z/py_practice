# 值可以是任何数据类型，key必须是字符串，数字，元组
dict1 = {}
print(dict1,type(dict1))
dict1 = dict()
print(dict1,type(dict1))
dict1 = {1:1,"name" : "张三",("a","b") : ("c","d")}
print(dict1,type(dict1))