# 写入文件,写入可以指定格式
w = open("test2.txt", mode="w", encoding="utf-8")
# 需要自己加换行符
w.write("test2\n")
w.write("test2\n")
w.writelines(["list1\n", "list2\n"])
list1 = ["a", "b", "c"]
list1 = map(lambda a: a + "\n", list1)
w.writelines(list1)
w.close()

r = open("test2.txt", mode="r", encoding="utf-8")
print(r.read())

# 追加写入
f = open("test2.txt", mode="a",encoding="utf-8")

f.write("test")

f.close()
