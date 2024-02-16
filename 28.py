import turtle
import random

turtle.setup(600, 600)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.shape("turtle")
turtle.register_shape("house.gif")
t2.shape("house.gif")



t1.penup()
t2.penup()



a = random.randint(-300,300)
b=random.randint(-300,300)

c = random.randint(-300,300)
d=random.randint(-300,300)

t1.goto(a,b)
t2.goto(c,d)


def a():
    dis = t1.distance(t2)
    print(dis)
    if dis < 30:
        print("到家了")
        turtle.bye()


def ahead():
    t1.penup()
    t1.forward(10)
    a()
    


def back():
    t1.penup()
    t1.backward(10)
    a()

def left():
    t1.penup()
    t1.left(30)


def right():
    t1.penup()
    t1.right(30)







turtle.listen()
turtle.onkeypress(ahead,"Up")
turtle.onkeypress(back,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")




