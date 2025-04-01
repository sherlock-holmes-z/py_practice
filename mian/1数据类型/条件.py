num = 10
if num > 10:
    print("1")
elif num > 5:
    print("2")
    print("22")
else:
    print("3")

# py3.10版本之后才会有, case _表示匹配所有
match num :
    case 1:
        print("1")
    case 2:
        print("2")
    case _:
        print("3")