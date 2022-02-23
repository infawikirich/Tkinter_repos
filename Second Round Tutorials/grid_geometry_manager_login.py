from tkinter import *
from tkinter import ttk


win = Tk()
win.title("Geometry Management")
win.title("Layout management")
win.geometry("300x300")
win.resizable(2, 2)

#configure the grid
win.columnconfigure(0, weight = 1)
win.columnconfigure(1, weight = 3)
win.columnconfigure(2, weight = 2)


#username
nameLabel = ttk.Label(win, text = "Username :")
nameLabel.grid(column = 0, row = 0, sticky = W, padx = 5, pady = 5)

nameEntry = ttk.Entry(win)
nameEntry.grid(column = 1, row = 0, sticky = EW, padx = 5, pady = 5, columnspan = 3)


# password
pswdLabel = ttk.Label(win, text = "Password :")
pswdLabel.grid(column = 0, row = 1, sticky = W, padx = 5, pady = 5)

pswdEntry = ttk.Entry(win, show = "*")
pswdEntry.grid(column = 1, row = 1, sticky = EW, padx = 5, pady = 5, columnspan = 3)


# login button
loginBtn = ttk.Button(win, text = "Login")
loginBtn.grid(column = 2, row = 3, sticky = EW, pady = 5, padx = 5)

win.mainloop()