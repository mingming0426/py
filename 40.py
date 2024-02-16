# for i in range(0,5):
#     for j in range(i,5-1):
#         print(" ",end="")
#     for a in range(0,i*2+1):
#         print("*",end="")
#     print(" ")


import turtle
import time
import random

turtle.setup(1100, 600)
turtle.bgpic("背景.gif")

colorList = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
turtle.tracer(False)


def fireworks(x, y):
    # 烟花尾
    color = random.choice(colorList)

    # 烟花球
    tList = []
    for i in range(20):
        t = turtle.Turtle()
        t.color(color)
        t.setheading(i * 18)
        t.penup()
        t.goto(x, y)
        t.forward(30)
        tList.append(t)
    turtle.update()
    # 绽放烟花球
    for i in range(50):
        for t in tList:
            t.forward(5)
        turtle.update()
        time.sleep(0.01)
    # 隐藏烟花球
    for t in tList:
        t.hideturtle()
    turtle.update()




turtle.listen()  # 开始监测事件
turtle.onscreenclick(fireworks)  # 监测鼠标点击事件
