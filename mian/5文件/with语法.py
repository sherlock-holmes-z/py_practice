# 使用with语句可以不用执行close方法
with open("test2.txt", mode="r", encoding="utf-8") as f:
    print(f.read())
