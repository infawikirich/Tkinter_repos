
from tkinter import *
from tkinter import ttk


win = Tk()

win.geometry("400x400")


label = ttk.Label(win, text = "Starting...")
label.grid()
label.bind("<Enter>", lambda e: label.configure(text = "Moved mouse inside"))

label.bind("<Leave>", lambda e: label.configure(text = "Moved mouse outside"))

label.bind("<ButtonPress-1>", lambda e: label.configure(text = "Clicked left mouse buttton"))

label.bind("<3>", lambda e: label.configure(text = "Clicked right mouse button"))

label.bind("<Double-1>", lambda e: label.configure(text = "Double clicked"))

label.bind("<B3-Motion>", lambda e: label.configure(text = "right button drag to %d, %d" % (e.x, e.y)))


win.mainloop()