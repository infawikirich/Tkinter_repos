import tkinter as tk
from tkinter import ttk

# create a root window
win = tk.Tk()
#win.geometry("400x400")

# configure rows and columns
win.rowconfigure(0, weight=1)  # 10% of total height
win.rowconfigure(1, weight = 8)  # 80% of total height
win.rowconfigure(2, weight = 1)  # 10% of total height

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=3)
win.columnconfigure(2, weight = 1)

frame_top = tk.Frame(win, bg = 'red')
frame_middle = tk.Frame(win, bg = 'yellow')
frame_bottom = tk.Frame(win, bg = 'blue')
frame_left = tk.Frame(win, bg = "lightgreen")
frame_right = tk.Frame(win, bg = 'lightblue')

# placing in grid
frame_top.grid(row = 0, column = 1, sticky= tk.NSEW)
frame_middle.grid(row = 1, column =1, sticky = tk.NSEW)
frame_bottom.grid(row = 2, column = 1, sticky = tk.NSEW)
frame_left.grid(row = 0, column = 0, rowspan=3, sticky = tk.NSEW)
frame_right.grid(row = 0, column = 2, rowspan=3, sticky = tk.NSEW)


frame_top.columnconfigure(0, weight = 1)
frame_top.columnconfigure(1, weight=3)
frame_top.columnconfigure(2, weight = 1)


label1 = ttk.Label(frame_top, text = "frame_top")
label1.grid(row = 0, column = 0, padx = 10, pady = 2)

label2 = ttk.Label(frame_top, text = 'frame_middle')
label2.grid(row = 0, column = 1, padx = 10, pady = 2)

label3 = ttk.Label(frame_top, text = "frame_bottom")
label3.grid(row = 0, column = 2, padx = 10, pady = 2)



win.mainloop()