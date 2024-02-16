a = int(input("语文："))
b = int(input("数学："))
c = int(input("英语："))
d = a + b + c
if d >= 270:
    print(d)
    print("优秀")
if d < 270:
    if d >= 240:
        print(d)
        print("良好")
if d < 240:
    if d >= 180:
        print(d)
        print("合格")
if d < 180:
    print(d)
    print("不合格")

