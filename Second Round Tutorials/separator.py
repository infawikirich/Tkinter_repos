import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.geometry("300x200")
win.resizable(False, False)
win.title("Separator Widget Demo")


ttk.Label(win, text = "First Label").pack()

separator = ttk.Separator(win, orient = 'horizontal')
separator.pack(fill = 'x')
ttk.Label(win, text = "Second Label").pack()


win.mainloop()