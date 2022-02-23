#!/usr/bin/python3


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# create a window to put widgets
win = Tk()



btn = Button(win, text = "Simple", bg = "red", fg = "yellow", font="Times", justify = "center")
btn.pack(side = TOP)

#messagebox.showinfo(message = "This is button")

print(btn.configure())

# create a loop for the code to continue running
win.mainloop()