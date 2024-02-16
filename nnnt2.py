from tkinter import Tk, Canvas

root = Tk()
c = Canvas(root, width=800, height=400)
c.configure(bg='blue', highlightthickness=0)
c.pack()
root.mainloop()
