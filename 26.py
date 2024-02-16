# # def fun(x):
# #     if x%2==0:
# #         print(str(x)+"是偶数")
# #     else:
# #         print(str(x)+"是奇数")
# # fun(6)
#
#
# import turtle as t
#
# # 选择背景图片
# t.bgpic("打字游戏.png")
#
#
#
#
# # 定义画雨滴的函数
# def draw_star(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor("red")
#     t.begin_fill()
#
#     for i in range(5):
#         t.forward(60)
#         t.left(144)
#     # t.right(90)
#     # t.circle(40, 180)
#     # t.right(90)
#
#     t.end_fill()
#
#
# xlist = []
# ylist = []
#
#
# def selectstar(x, y):
#     xlist.append(x)
#     ylist.append(y)
# def test():
#     t.clear()
#
#
#
#
#
#
#
# # 监听鼠标点击事件
# t.listen()
# t.onscreenclick(draw_star,btn=3)  # 防止多次点击触发多个雨滴
# t.onkeypress(test, 'space')
#
# t.speed(0)  # 设置绘制速度
# t.mainloop()


def fun(x):
    if x%4==0:
        print(str(x)+"年是闰年")
    else:
        print(str(x)+"年不是闰年")
fun(2024)

