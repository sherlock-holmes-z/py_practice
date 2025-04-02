# 打开文件
f = open("test.txt")

# mode表示打开文件的模式，默认r只读，
#   w写，写之前清空内容，文件不存在会创建新文件
#   a追加，在原文本中继续写，文件不存在会创建新文件
f1 = open("test.txt",mode="r",encoding="UTF-8")

# 读取文件
context = f.read()
print(context)

# 读取一行
print(f1.readline())

# 将每行数据读出存到一个字典里
print(f1.readlines())

# 关闭文件
f.close()
