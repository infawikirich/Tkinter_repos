import tkinter as tk
from tkinter import Menu


# root window
win = tk.Tk()

win.title("Menu Demo 1")


# create a menubar
menubar = Menu(win)
win.config(menu = menubar)

# create a menu
file_menu = Menu(menubar, tearoff = False)

# add a menu item to the menu
file_menu.add_command(
    label = "Exit",
    command=win.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label = "File",
    menu = file_menu
)

win.mainloop()
