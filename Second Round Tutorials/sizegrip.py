import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("Sizegrip Demo")
win.geometry("300x200")
win.resizable(True, True)


# grid layout
win.columnconfigure(0, weight = 1)
win.rowconfigure(0, weight = 1)


# create the sizegrip
sg = ttk.Sizegrip(win)
sg.grid(row = 1, sticky = tk.SE)



win.mainloop()