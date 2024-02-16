import random


a = int(input('请输入你猜的数字，石头（1），剪刀（2），布（3）'))
b = random.randint(1, 3)
print('a出的是：', ['石头', '剪刀', '布'][(a - 1)])
print('b出的是：', ['石头', '剪刀', '布'][(b - 1)])
if (a == 1):
    if (b == 1):
        print('平局')
    elif (b == 2):
        print('a赢')
    elif (b == 3):
        print('b赢')
    else:
        print('故障')
elif (a == 2):
    if (b == 1):
        print('b赢')
    elif (b == 2):
        print('平局')
    elif (b == 3):
        print('a赢')
    else:
        print('故障')
elif (a == 3):
    if (b == 1):
        print('a赢')
    elif (b == 2):
        print('b赢')
    elif (b == 3):
        print('平局')
    else:
        print('故障')
else:
    print('故障')
