users = [
    {"name": "zhangsan", "password": "123456"},
    {"name": "lisi", "password": "234567"},
    {"name": "wangwu", "password": "123456"}
]

not_allow = {"wangwu"}

username = str(input("账户："))
password = str(input("密码："))

if username in not_allow:
    print("禁止登录")

for i in users:
    if username == i["name"]:
        if password == i["password"]:
            print("登录成功")
        else:
            print("密码错误")
        break
else:
    print("用户不存在")