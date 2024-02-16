import tkinter
import tkinter.messagebox

window = tkinter.Tk()  # 创建窗口
window.geometry("600x600")  # 设置窗口大小
window.title("读心术")  # 设置窗口标题

# 添加背景图片
photo = tkinter.PhotoImage(file="pic.png")  # 将图片加载进程序中
lab1 = tkinter.Label(image=photo)  # 创建图片标签
lab1.place(x=0, y=0)  # 设置图片位置

# 显示文字
lb2 = tkinter.Label(text="游戏规则：", font=("微软雅黑", 30))
lb2.place(x=10, y=10)
lb2 = tkinter.Label(text="1、请从1～31中随意选取一个数字，记住它", font=("微软雅黑", 15))
lb2.place(x=10, y=60)
lb3 = tkinter.Label(text="2、点击开始按钮，你心中的那个数字即将出现在屏幕上", font=("微软雅黑", 15))
lb3.place(x=10, y=90)

# 创建按钮，并为按钮绑定功能
btn = tkinter.Button(text="开始", font=("微软雅黑", 30), width=10)
btn.place(x=200, y=300)