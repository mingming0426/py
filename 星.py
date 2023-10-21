import turtle
import random
import time

turtle.bgpic("背景.png")
turtle.setup(800, 600)
turtle.tracer(False)
t1 = turtle.Turtle()


def star5(x, y):
    size = random.randint(10, 100)
    # 画五角星
    t1.hideturtle()
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.color("yellow")
    t1.begin_fill()
    for i in range(5):
        t1.forward(size)
        t1.right(144)
    t1.end_fill()
    turtle.update()


def star4(x, y):
    sze = random.randint(10, 70)
    # 画四角星
    t1.hideturtle()
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.color("yellow")
    t1.begin_fill()
    for i in range(4):
        t1.left(75)
        t1.forward(sze)
        t1.right(165)
        t1.forward(sze)
    t1.end_fill()
    turtle.update()


xlist = []
ylist = []


# 随机选择画五角星或四角星
def selectstar(x, y):
    xlist.append(x)
    ylist.append(y)
    num = random.randint(0, 1)
    if num == 0:
        star5(x, y)
    else:
        star4(x, y)


def test():
    print("空格被按下！")
    # 星星闪动
    while True:
        t1.clear()
        for i in range(len(xlist)):
            x = xlist[i]
            y = ylist[i]
            num = random.randint(0, 1)
            if num == 0:
                star5(x, y)
            else:
                star4(x, y)
        time.sleep(0.15)


turtle.listen()  # 开始监测事件
turtle.onscreenclick(selectstar)  # 监测鼠标点击事件
turtle.onkeypress(test, 'space')  # 监测键盘事件

import turtle

# turtle.setup(800, 600)
turtle.tracer(False)
t1 = turtle.Turtle()


def s4(x, y):
    # 画正方形
    t1.hideturtle()
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    for i in range(4):
        t1.forward(40)
        t1.left(90)
    turtle.update()


def test():
    t1.clear()


turtle.listen()  # 开始监测事件
turtle.onscreenclick(s4)  # 监测鼠标点击事件
turtle.onkeypress(test, 'space')  # 监测键盘事件

