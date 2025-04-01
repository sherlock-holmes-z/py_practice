str1 = "hello world"
print(len(str1))
# min是空格
print(max(str1),min(str1))

# 从字符串第一位一次向后比较
print("abcd" < "abce")
print("caaa" < "bzzz")

for i in str1:
    print(i)
for i,s in enumerate(str1):
    print(i,s)
for i in range(len(str1)):
    print(i,str1[i])

print(str1.islower(),str1.isupper())
print(str1.count("0"),str1.strip())
print(str1.split(" "))
print(str1.index("o",5))
print(str1.find("o",0,10))
print(str1.find("z"))
# print(str1.index("z")) # index找不到会报错


# 使用符号拼接成字符串
print("#".join(["1","2","3","4"]))
print("#".join(("1","2","3","4")))

# 判断数字，字母
for i in str1:
    print(i.isdigit(),i.isalpha())