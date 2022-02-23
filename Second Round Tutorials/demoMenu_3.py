from tkinter import Tk, Menu


# root window
win = Tk()
win.geometry("320x150")
win.title("Menu Demo")


# create a menubar
menubar = Menu(win)
win.config(menu = menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label = "New")
file_menu.add_command(label = "Open...")
file_menu.add_command(label = "Close")
file_menu.add_separator()


# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label = "Keyboard Shortcuts")
sub_menu.add_command(label = "Color Themes")

# add the file menu to the menubar
file_menu.add_cascade(
    label = "Preferences",
    menu = sub_menu
)

menubar.add_cascade(
    label = "File",
    menu = file_menu,
    underline = 0
)

# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)


help_menu.add_command(label = "Welcome")
help_menu.add_command(label = "About")


# add the Help menu to the menubar
menubar.add_cascade(
    label = "Help",
    menu = help_menu,
    underline= 0
)

win.mainloop()