#!/usr/bin/python3


from tkinter import *
from tkinter import messagebox


# create a window for the tkinter
win = Tk()

# set the screen size
win.geometry("300x200")


def btn1Func():
    messagebox.showinfo("Welcome to Vispad Institute of Technology")

def btn2Func():
    messagebox.showwarning("As you have bee admitted tread carefully")

def btn3Func():
    messagebox.showerror("You pushed the wrong button")

def btn4Func():
    messagebox.showinfo("We can't wait to have you on board")


btn1 = Button(win, text = "Red Button", fg = "red", bg = "blue", pady = 10, font = "Times", command = btn4Func)
btn1.pack(side = LEFT)

btn2 = Button(win, text = "Blue Button", fg = "blue", bg = "black", pady = 10, font = "Times", command = btn2Func)
btn2.pack(side = RIGHT)

btn3 = Button(win, text = "Green Button", fg = "green", bg = "red", pady = 10, font = "Times", command = btn1Func)
btn3.pack(side = TOP)

btn4 = Button(win, text = "Yellow Button", fg = "yellow", bg = "white", pady = 10, font = "Times", command = btn3Func)
btn4.pack(side = BOTTOM)


win.mainloop()





