#!/usr/bin/python3

from tkinter import *


parent = Tk()

text = Text(parent)
text.insert(INSERT, 'Name...')
text.insert(END, "Salary...")

text.pack()

text.tag_add("Write Here", '1.0', '1.4')
text.tag_add("Click Here", '1.8', '1.13')

text.tag_config("Write Here", background = 'yellow', foreground = 'black')
text.tag_config('Click Here', background = 'black', foreground = 'white')


parent.mainloop()