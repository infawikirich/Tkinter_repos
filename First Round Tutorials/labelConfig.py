import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("Configuring a label")
win.resizable(False, False)
win.geometry("300x200")


# create a frame to hold the other widgets
frame = ttk.Frame(win)


def dosomtehing():
    myLabel.config(text = "Goodbye World")


options = {"pady" :10, "padx" : 5}

# create label
myLabel = ttk.Label(frame, text = "Hello World")
myLabel.pack(**options)


# create button
myButton = ttk.Button(frame, text = "Clicked Me", command= dosomtehing)
myButton.pack(**options)

# pack the frame
frame.pack(**options)

win.mainloop()







