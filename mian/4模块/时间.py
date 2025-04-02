import time

# 时间戳
t = time.time()
print(t)
# 结构化时间
t = time.localtime()
print(t)
print(t.tm_year)
print(t.tm_mon)
print(t.tm_mday)

# 格式化时间为字符串
s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(s)
