#!/usr/bin/python3

from tkinter import *

# create an object
tk = Tk()


tk.geometry("400x250")

name = Label(tk, text = 'Name').place(x = 30, y = 50)
email = Label(tk, text = 'Email').place(x = 30, y = 90)
password = Label(tk, text = 'Password').place(x = 30,y=130)

entry_1 = Entry(tk).place(x = 80, y = 50)
entry_2= Entry(tk).place(x = 80, y = 90)
entry_3= Entry(tk).place(x = 95, y=130)

checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()

checkbtn1 = Checkbutton(tk, text = 'C', variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10).place(x=240, y = 50)
checkbtn2 = Checkbutton(tk, text = 'C++', variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10).place(x=248, y = 80)
checkbtn3 = Checkbutton(tk, text = 'Python', variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10).place(x=255, y = 110)

tk.mainloop()