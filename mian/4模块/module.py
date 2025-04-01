# import my_module
#
# r = my_module.add(1,2)
# print(r)
#
# print(my_module.author)


# 直接指定导入的方法及变量，使用时就不用加原module名了
# as可以重命名，防止和本地方法冲突
from my_module import add, author,m as f

r = add(1, 2)
print(r)
print(author)
f()
