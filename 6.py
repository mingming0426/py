a = 0
while True:
    a+=1
    print(a)
    if a==10:
        break
#第三题
while True:
    a+=1
    if a%3==0:
        print(str(a)+"是3的倍数")
    if a==100:
        break
#第四题
i = 1000
while True:
    i = i - 1
    if i >= 100:
        if i == 555:
            continue
        elif i % 37 == 0:
            print(i)
