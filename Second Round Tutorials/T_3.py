#!/usr/bin/python3


from tkinter import *

# create an object of the tkinter

win = Tk()

# set the geometry of the canvas
win.geometry("400x250")

name = Label(win, text = "Name").place(x = 30, y = 50)
email = Label(win, text = "Email").place(x = 30, y = 90)
password = Label(win, text = "Password").place(x=30, y = 130)

nameEntry = Entry(win).place(x = 95, y = 50)
emailEntry = Entry(win).place(x = 95, y = 90)
passwordEntry = Entry(win).place(x = 95, y = 130)


# create a mainloop for the program
win.mainloop()
