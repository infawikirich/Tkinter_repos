#!/usr/bin/python3

from tkinter import *

# create the window surface
win = Tk()


win.geometry("400x400")


canvas = Canvas(win, bg = 'red', width = 400, height = 400)
canvas.pack()


win.mainloop()

