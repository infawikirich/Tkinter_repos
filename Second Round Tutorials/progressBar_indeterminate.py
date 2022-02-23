import tkinter as tk
from tkinter import ttk


# root window
win = tk.Tk()
win.geometry("300x200")
win.title('Progressbar')
win.resizable(False, False)


win.grid()

# progressbar
pb = ttk.Progressbar(
    win,
    orient = "horizontal",
    mode = "indeterminate",
    length = 280
)

# place the progressbar
pb.grid(column = 0, row = 0, columnspan = 2, padx = 10, pady = 20)

# start button
start_button = ttk.Button(
    win,
    text = "Start",
    command = pb.start
)

start_button.grid(column = 0, row = 1, padx = 10, pady = 10, sticky = tk.E)


# stop button
stop_button = ttk.Button(win, text = "Stop", command = pb.stop)
stop_button.grid(column = 1, row = 1, padx = 10, pady = 10, sticky = tk.E)


win.mainloop()