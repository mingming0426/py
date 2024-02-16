import turtle
import time
import random

turtle.setup(1100, 600)
turtle.bgpic("背景.gif")

colorList = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
turtle.tracer(False)
def fireworks(angle,x,y):
    # 烟花尾
    color = random.choice(colorList)
    w = turtle.Turtle()
    w.color(color)
    w.pensize(5)
    w.hideturtle()
    w.penup()
    w.goto(x,y)
    w.setheading(angle)
    w.pendown()
    for i in range(50):
        w.forward(2)
        turtle.update()
        time.sleep(0.01)
    w.clear()
    x = w.xcor()
    y = w.ycor()

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
    #隐藏烟花球
    for t in tList:
        t.hideturtle()
    turtle.update()
# fireworks(45,-175,-30)
# fireworks(135,150,-30)
posList=[[45,-175,-30],[90,-90,30],[90,0,50],[90,90,30],[135,150,-35]]
while True:
    pos=random.choice(posList)
    fireworks(pos[0],pos[1],pos[2])
