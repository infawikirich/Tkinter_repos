import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("PanedWindow")
win.geometry("300x200")

# change style to classic (Windows only)
# to show sash and handle
style = ttk.Style()
style.theme_use('classic')


# paned Window
pw = ttk.Panedwindow(orient = tk.HORIZONTAL)

# Left listbox
left_list = tk.Listbox(win)
left_list.pack(side = tk.LEFT)
pw.add(left_list)

# right listbox
right_list = tk.Listbox(win)
right_list.pack(side = tk.LEFT)
pw.add(right_list)


# place the panedWindow on the root window
pw.pack(fill = tk.BOTH, expand = True)


win.mainloop()

