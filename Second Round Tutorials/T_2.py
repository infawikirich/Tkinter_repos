#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

# create a window
win = Tk()
win.title("Event Binding")
win.attributes("-topmost", 1)


def return_pressed(event):
    print("Return key pressed")

def log(event):
    print(event)


firstname = ttk.Label(win, text = "First name").grid(row = 0, column = 0)
firtNameEntry = Entry(win).grid(row = 0, column = 1)

secondtname = ttk.Label(win, text = "Surname").grid(row = 0, column = 6)
scondNameEntry = ttk.Entry(win).grid(row = 0, column = 9)

email = ttk.Label(win, text = "Email").grid(row = 2, column = 0)
emailEntry = ttk.Entry(win).grid(row = 2, column = 1)

password = ttk.Label(win, text = "Password").grid(row = 4, column = 0)
passwordEntry = ttk.Entry(win).grid(row = 4, column = 1)

submit = ttk.Button(win, text = "Submit").grid(row = 6, column = 0)
submit.bind("<Return>", return_pressed)
submit.bind("<Return>", log, add="+")
submit.focus()

# create mainloop for the program
win.mainloop()