import tkinter as tk
from tkinter import  ttk
from tkinter.colorchooser import askcolor



win = tk.Tk()
win.title("Tkinter Color Chooser")
win.geometry("300x150")


def change_color():
    colors = askcolor(title = "Tkinter Color Chooser")
    win.configure(bg = colors[1])


ttk.Button(
    win,
    text = "Select a Color",
    command = change_color).pack(expand = True)


win.mainloop()