# 异常未触发时，性能开销非常小，在高频触发异常的地方最好使用if else去判断

# else在没有异常时执行，finally无论什么情况都会执行
try:
    print("normal")
    i = int(input("input:"))
    print(i)
except:
    print("error:")
else:
    print("else")
finally:
    print("finally")

print("*" * 10)

try:
    i = int(input("input:"))
    i = 5 / i
except ZeroDivisionError as e:
    print("除数不能为0异常:", e)
except Exception as e:
    print("异常：", e)
else:
    print("else")
finally:
    print("finally")

print("*" * 10)

# raise 手动抛出异常
try:
    i = int(input("input:"))
    if i < 10 :
        raise Exception("number is less than 10")
except Exception as e:
    print(e)