import random
name=input("请输入姓名：")
while True:
    a=random.randint(1,3)#1=石头，2=剪刀，3=布
    user=input("请输入出的（石头/剪刀/布）：")

    if a == 1:
        s="石头"
    elif a == 2:
        s="剪刀"
    elif a == 3:
        s="布"
    if user == s:
        print("平局！")
    print("电脑出的："+s)

    if s == "石头"and user == "剪刀":
        print("电脑获胜！")

    elif s == "剪刀"and user == "布":
        print("电脑获胜！")

    elif s == "布"and user == "石头":
        print("电脑获胜！")

    elif s == "石头" and user == "布":
        print("玩家"+name+"获胜！")

    elif s == "剪刀" and user == "石头":
        print("玩家"+name+"获胜！")

    elif s == "布" and user == "剪刀":
        print("玩家"+name+"获胜！")