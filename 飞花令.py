import time
import string
import tkinter  # 导入tkinter模块用于创建GUI
import tkinter.messagebox  # 导入tkinter.messagebox模块用于显示消息框

# 创建主窗口
window = tkinter.Tk()
window.geometry("700x500")  # 设置窗口大小
window.title("飞花令")  # 设置窗口标题

# 创建用户界面元素：标签和输入框
label1 = tkinter.Label(window, text="飞花令", font=("微软雅黑", 20))
label1.pack(pady=50)

label2 = tkinter.Label(window, text="请说一句带月的诗词吧：（用空格将前后两句隔开哦）", font=("微软雅黑", 20))
label2.pack(pady=0)

entry1 = tkinter.Entry(window, font=("微软雅黑", 20), width=80)
entry1.pack()


# 函数：判断输入是否为中文
def is_Chinese(words):
    """
    判断字符串中是否只包含中文字符。

    参数:
    words (str): 需要判断的字符串。

    返回:
    bool: 如果字符串中只包含中文字符，返回True；否则返回False。
    """
    for ch in words:
        if ord(ch) < 13312 or ord(ch) > 40956:
            return False
    return True


# 从文件读取诗词库
f = open("诗词库.txt", encoding="gbk")
computerstore = f.readlines()
f.close()
computerstore = [i.strip("\n") for i in computerstore]
computerstoreDel = []
for k in computerstore:
    for i in k:
        if i in string.punctuation:
            k = k.replace(i, "")
    computerstoreDel.append(k)
Dict = dict(zip(computerstoreDel, computerstore))
sharedStore = []
count = 3  # 超时次数
Round = 5  # 游戏回合数
time_start = time.time()


# 主游戏逻辑函数
def panduan(scount, sRound):
    """
    用户和计算机进行飞花令游戏的主逻辑函数。

    参数:
    scount (int): 用户的超时次数。
    sRound (int): 游戏剩余回合数。

    无返回值。
    """
    global count, Round, time_start
    while True:
        user = entry1.get()
        user = ''.join(user.split())  # 去除输入中的空格
        n = len(user)
        if n < 1:
            break
        # 输入判断逻辑
        while True:
            if not is_Chinese(user):
                tkinter.messagebox.showinfo("提示", "出现了汉字之外的字符哦，请再说一句吧：")
                entry1.delete(0, tkinter.END)
                break
            elif n < 8:
                tkinter.messagebox.showinfo("提示", "这句不完整哦，再补充下吧：")
                entry1.delete(0, tkinter.END)
                break
            elif "月" not in user:
                tkinter.messagebox.showinfo("提示", "要含有关键字“月”哦，检查一下再输入一次吧：")
                entry1.delete(0, tkinter.END)
                break
            elif user in sharedStore:
                tkinter.messagebox.showinfo("提示", "这句之前出现过了哦，说句新的吧：")
                entry1.delete(0, tkinter.END)
                break
            elif user not in computerstoreDel:
                tkinter.messagebox.showinfo("提示", "这句是诗词吗？不然再说一句吧：")
                entry1.delete(0, tkinter.END)
                break
            else:
                break

        # 更新游戏状态
        time_end = time.time()
        sharedStore.append(user)
        print(user);

        computerstoreDel.remove(user)
        output = computerstoreDel.pop(0)
        sharedStore.append(output)
        tkinter.messagebox.showinfo("", Dict[output])
        entry1.delete(0, tkinter.END)
        time_cost = time_end - time_start
        if time_cost > 30:
            count -= 1
            tkinter.messagebox.showwarning("警告", "已超时，超时机会还剩{}次".format(count))
        if scount < 0:
            tkinter.messagebox.showwarning("警告", "很遗憾，你输了哦")
            window.destroy()
            break

        sRound -= 1
        Round = sRound
        tkinter.messagebox.showwarning("警告", "剩余回合数:{}".format(Round))
        time_start = time.time()

        if sRound == 0:
            tkinter.messagebox.showinfo("恭喜", "恭喜，你赢得了这此飞花令！")
            window.destroy()
            break


# 函数：启动游戏逻辑
def change_b2(count, Round):
    panduan(count, Round)


# 创建并添加“确定”按钮到窗口
btn2 = tkinter.Button(window, text="确定", font=("微软雅黑", 20), width=20, command=lambda: change_b2(count, Round))
btn2.pack()

# 运行窗口的主循环
window.mainloop()
