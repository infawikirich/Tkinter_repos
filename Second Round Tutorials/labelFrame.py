import tkinter as tk
from tkinter import ttk



# root window
win = tk.Tk()


# configure the root window
win.geometry("300x200")
win.resizable(False, False)
win.title("LabelFrame Demo")

# label Frame
lf = ttk.Labelframe(win, text = "Alignment")
lf.grid(column = 0, row = 0, padx = 20, pady = 20)

alignment_var = tk.StringVar()
alignments = ("Left", "Center", "Right")


# create radio buttons and place them on the label frame

grid_column = 0
for alignment in alignments:
    # create a radio button
    radio = ttk.Radiobutton(lf, text = alignment, value = alignment, variable = alignment_var)
    radio.grid(column = grid_column, row = 0, ipadx = 10, ipady = 10)

    #grid column
    grid_column += 1



win.mainloop()

