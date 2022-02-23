"""
This program uses tkinter grid geometry manager to place object
in the root window

"""

import tkinter as tk


# create a base window
win = tk.Tk()
win.title("Grid Geometry Manager")
win.geometry("320x300+300+200")
win.resizable(False, False)


for i in range(5):
    for j in range(5):
        frame = tk.Frame(
            win,
            relief= tk.RAISED,
            borderwidth=1
        )
        frame.grid(row = i, column = j, padx =2, pady = 2)
        label = tk.Label(frame, text = f"Row {i}\nColumn {j}")
        label.pack()







# looop for the program
win.mainloop()