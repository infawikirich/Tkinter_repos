from tkinter import Tk, Frame, Menu


# root window
win = Tk()
win.geometry("320x150")
win.title("Menu Demo")

# create a menubar
menubar = Menu(win)
win.config(menu = menubar)

# create  the file_menu
file_menu = Menu(
    menubar,
    tearoff = 0
)


# add menu items to the File menu
file_menu.add_command(label = "New")
file_menu.add_command(label = "Open...")
file_menu.add_command(label = "Close")
file_menu.add_separator()


# add Exit menu item
file_menu.add_command(
    label='Exit',
    command = win.destroy
)

# add the file menu to the menubar
menubar.add_cascade(
    label = "File",
    menu = file_menu
)

# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label = "Welcome")
help_menu.add_command(label = 'About...')


# add the help menu to the menubar
menubar.add_cascade(
    label = "Help",
    menu = help_menu
)


win.mainloop()