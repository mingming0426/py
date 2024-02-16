import tkinter
import tkinter.messagebox
# window = tkinter.Tk()
# window.geometry("600x400")
# window.title("贴图片")
# photo = tkinter.PhotoImage(file="pic.png")
# lab1 = tkinter.Label(image=photo)
# lab1.place(x=0, y=0)

window = tkinter.Tk()
window.geometry("200x100")

b = tkinter.Label(window,text="进制转换", font=("微软雅黑", 10))
b.pack()
c = tkinter.Entry(window,font=("微软雅黑", 10))
c.pack(pady=10)

def guess():
    e = c.get()
    print(e)
    a = list(e)
    print(a)
    d=a[0]*16+a[1]*8+a[2]*4+a[3]*2+a[4]*1

    print(d)
    tkinter.messagebox.showinfo("见证奇迹的时刻", "转换为十进制数后是{}".format(d))


btn = tkinter.Button(text="开始", font=("微软雅黑", 10), width=10, command=guess)
btn.place(x=50, y=50)





