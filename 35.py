import tkinter  # 导入tkinter模块
import tkinter.messagebox  # 导入tkinter.messagebox模块

window = tkinter.Tk()  # 创建窗口
window.geometry("400x500")  # 设置窗口大小
window.title("消息窗口")  # 设置窗口标题
label1 = tkinter.Label(window, text="请输入需要发送的内容", font=("微软雅黑", 20))
# 粘贴文字
label1.pack(pady=50)

# 创建输入框
entry1 = tkinter.Entry(window, font=("微软雅黑", 20))
entry1.pack()


def a():
    b = entry1.get()
    tkinter.messagebox.showinfo("提示", b+"发送成功")



# 按钮
btn1 = tkinter.Button(window, text="发送", font=("微软雅黑", 20), width=20,command=a)
btn1.pack(pady=20)

