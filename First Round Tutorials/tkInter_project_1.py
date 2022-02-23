#!/usr/bin/python3

from tkinter import *

parent = Tk()

parent.geometry('200x150')

# creating a simple canvas
canvas = Canvas(parent, bg='lightgreen', height = 300)


messagebox = Label(parent, text = 'Welcome to Vision')
messagebox.pack(side = BOTTOM)

def fun():
    messagebox.configure(text = 'Red Button clicked')

redbutton = Button(parent, text='Red', fg = 'red', pady=10, command=fun)
redbutton.pack(side = LEFT)

greenbutton = Button(parent, text='Black', fg = 'black', pady=10)
greenbutton.pack(side = RIGHT)

bluebutton = Button(parent, text='Blue', fg = 'blue', pady=10)
bluebutton.pack(side = TOP)

blackbutton = Button(parent, text='Green', fg = 'red', pady=10)
blackbutton.pack(side = BOTTOM)



canvas.pack()

parent.mainloop()

