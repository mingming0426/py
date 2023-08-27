user = input("输入：")
if user == "风之石" or user == "火之石" or user == "水之石":
    print("魔法门开启!")
else:
    print("释放黑魔法!")

a = ["风之石", "火之石", "水之石"]
user = input("输入（按顺序）：")
user1 = input("输入：")
user2 = input("输入：")
if user in a:
    a.pop(a.index(user))
    if user1 in a:
        a.pop(a.index(user1))
        if user2 in a:
            print("魔法门开启!")
            user3 = input("进了几个人：")
            persen = user3
            for i in range(0, int(persen)):
                if i == 100:
                    print("魔法门关闭")
                    break
                i += 1

else:
    print("释放黑魔法!")

# 4
while True:
    ele = 0
    ele = input("有几格电？(100以内)：")
    a = int(ele)
    if int(ele) > 100:
        print("无效的输入")
    if int(ele) <= 20:
        print("请充电！")
    if int(ele) >= 20:
        if int(ele) <= 100:
            print("开始巡视")
            a -= 10
            while True:
                b = input("有没有障碍物：")
                if b == "有":
                    print("右转30°")
                    a -= 10
                    print(a)
                else:
                    print()
                cd = input("有没有污渍：")

                if cd == "有":
                    a -= 10
                    print("开始擦地")
                    print(a)
                    if b == "有":
                        print("右转30°")
                        print(a)
                        a -= 10
                    else:
                        print()
                elif cd == "没有":
                    print("继续巡视")
                else:
                    print("不要乱输")
                if a <= 20:
                    print("请充电！")
                    break
