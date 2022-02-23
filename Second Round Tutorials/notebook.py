import tkinter as tk
from tkinter import ttk


# root window
win = tk.Tk()
win.geometry("400x300")
win.title("Notebook Demo")

# create a notebook
notebook = ttk.Notebook(win)
notebook.pack(pady = 10, expand = True)

# create frames
frame1 = ttk.Frame(notebook, width = 400, height =280)
frame2 = ttk.Frame(notebook, width =400, height = 280)

frame1.pack(fill = 'both', expand = True)
frame2.pack(fill = "both", expand = True)

# add frames to notebook
notebook.add(frame1, text = "General Information")
notebook.add(frame2, text = 'Profile')


win.mainloop()


