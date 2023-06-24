import random

qipan = ("0|1|2\n-----\n3|4|5\n-----\n6|7|8\n-----\n")
print(qipan)


while True:
    user=input("请输入要落子的位置数：")
    if user == "esc":
        break
    if qipan.index(user)>=0:
        qipan = qipan.replace(str(user),"x")
        print(qipan)

        print("电脑下棋")
        a=random.randint(0,8)


        qipan = qipan.replace(str(a), "o")
        print(qipan)

    else:
        print("请重新落子")





