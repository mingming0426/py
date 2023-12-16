# import turtle
# import random
# turtle.tracer(False)
# turtle.setup(800, 600)
# turtle.color("red")
#
# turtle.register_shape("27py.gif")
# turtle.shape("27py.gif")
#
# def test():
#     x = random.randint(0, 800)
#     y = random.randint(0, 600)
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()
#     turtle.begin_fill()
#     for i in  range(5):
#         turtle.forward(100)
#         turtle.left(144)
#     turtle.end_fill()
#
#
#
# turtle.listen()  # 开始监测事件
# turtle.onkeypress(test, 'space')  # 监测键盘事件
#


import turtle

turtle.setup(800, 600)
turtle.bgpic("bg.gif")
df = 0
defen = str(df)

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("green")
t2 = turtle.Turtle()  # 兔子

turtle.register_shape("rabbit.gif")
t2.shape("rabbit.gif")
t2.penup()
t2.goto(100, 200)

turtle.register_shape("carrot.gif")
lb = turtle.Turtle()
lb.shape("carrot.gif")
lb.penup()
lb.goto(100, 200)

word = turtle.Turtle()
word.hideturtle()
word.penup()
word.goto(-350, 250)
word.pendown()
word.write("得分：" + defen, font=("微软雅黑", 20))


def ahead():
    t1.penup()
    t1.forward(10)


def back():
    t1.penup()
    t1.backward(10)


def left():
    t1.penup()
    t1.left(30)


def right():
    t1.penup()
    t1.right(30)


# def rr():
#     angle = t2.towards(t1)
#     print(angle)
#     t2.setheading(angle)
#     t2.forward(5)




def ahead2():
    t2.penup()
    t2.forward(10)


def back2():
    t2.penup()
    t2.backward(10)


def left2():
    t2.penup()
    t2.left(30)


def right2():
    t2.penup()
    t2.right(30)

turtle.listen()
turtle.onkeypress(ahead, "Up")
turtle.onkeypress(back, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

# while True:
#     rr()


turtle.listen()
turtle.onkeypress(ahead2, "w")
turtle.onkeypress(back2, "s")
turtle.onkeypress(left2, "a")
turtle.onkeypress(right2, "d")




"""import turtle
import random
turtle.shape("turtle")
colorList = ["red", "blue", "green", "yellow", "black", "pink", "orange"]
def test():
    idx=random.randint(0,len(colorList)-1)
    color=colorList[idx]
    turtle.color(color)


turtle.listen()  # 开始监测事件
turtle.onkeypress(test,'space')  #监测键盘事件"""





