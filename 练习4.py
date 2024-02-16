import turtle

#turtle.setup(800, 600)
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
turtle.onkeypress(test,'space')  #监测键盘事件
