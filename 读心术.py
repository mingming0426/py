import tkinter
import tkinter.messagebox

window = tkinter.Tk()  # 创建窗口
window.geometry("600x600")  # 设置窗口大小
window.title("读心术")  # 设置窗口标题

photo = tkinter.PhotoImage(file="pic.png")  # 加载图片
lab1 = tkinter.Label(image=photo)  # 创建图片标签
lab1.place(x=0, y=0)  # 设置图片位置

lb2 = tkinter.Label(text="游戏规则：", font=("幼圆", 30))
lb2.place(x=10, y=10)
lb2 = tkinter.Label(text="1、请从1--31中随意选取一个数字，记住它", font=("幼圆", 17))
lb2.place(x=10, y=55)
lb3 = tkinter.Label(text="2、点击开始按钮，你心中的那个数字即将出现在屏幕上", font=("幼圆", 17))
lb3.place(x=10, y=85)


def guess():
    tkinter.messagebox.showinfo("提示", "请先回到我的几个问题")
    res1 = tkinter.messagebox.askquestion("提问",
                                          "你心中想的数字是否存在于下面的数字中：16，17，18，19，20，21，22，23，24，25，26，27，28，29，30，31")
    res2 = tkinter.messagebox.askquestion("提问",
                                          "你心中想的数字是否存在于下面的数字中：8，9，10，11，12，13，14，15，24，25，26，27，28，29，30，31")
    res3 = tkinter.messagebox.askquestion("提问",
                                          "你心中想的数字是否存在于下面的数字中：4，5，6，7，12，13，14，15，20，21，22，23，28，29，30，31")
    res4 = tkinter.messagebox.askquestion("提问",
                                          "你心中想的数字是否存在于下面的数字中：2，3，6，7，10，11，14，15，18，19，22，23，26，27，30，31")
    res5 = tkinter.messagebox.askquestion("提问",
                                          "你心中想的数字是否存在于下面的数字中：1，3，5，7，9，11，13，15，17，19，21，23，25，27，29，31")
    reslist=[res1,res2,res3,res4,res5]
    num=0
    for i in reslist:
        if i =="yes":
            reslist[num]=1
            num+=1
        else:
            reslist[num]=0
            num+=1

    a=reslist[0]*16+reslist[1]*8+reslist[2]*4+reslist[3]*2+reslist[4]*1
    tkinter.messagebox.showinfo("见证奇迹的时刻", "你心中想的数字是：{}".format(a))




# 创建按钮
btn = tkinter.Button(text="开始", font=("幼圆", 30), width=10, command=guess)
btn.place(x=200, y=300)
