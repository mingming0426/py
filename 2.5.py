# user = int(input("输入数字："))
# lst = (i for i in range(user))
# s = sum(lst)
# print("计算出来的和是{}".format(s))


num = 0
for i in range(1, 10):
    for j in range(0, 10):
        print(str(i) + str(j), end=' ')
        num += 1
        if num == 20:
            print()
            num = 0