import turtle

turtle.color("aquamarine")
canvas = turtle.Screen()
pen = turtle.Turtle()

#
#
# def square():
#     for i in range(4):
#         turtle.left(90)
#         turtle.forward(100)
#
#
# turtle.listen()
# turtle.onkeypress(square(), "space")


turtle.begin_fill()
for i in range(3):
    turtle.forward(120)
    turtle.left(120)
turtle.right(90)
turtle.circle(60, 180)
turtle.end_fill()
turtle.penup()
turtle.forward(9999999999999999999999999999999999)

import turtle as t
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.withdraw()  # 隐藏Tkinter窗口

# 选择背景图片
t.bgpic("2243.png_860.png")


# 定义画雨滴的函数
def draw_raindrop(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("aquamarine")
    t.begin_fill()

    for i in range(3):
        t.forward(80)
        t.left(1200)
    t.right(90)
    t.circle(40, 180)
    t.right(90)

    t.end_fill()


xlist = []
ylist = []


def selectstar(x, y):
    xlist.append(x)
    ylist.append(y)


def test():
    t.clear()


# 监听鼠标点击事件
t.listen()
t.onscreenclick(draw_raindrop)  # 防止多次点击触发多个雨滴
t.onkeypress(test, 'space')

t.speed(0)  # 设置绘制速度
t.mainloop()
