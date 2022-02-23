import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("Configuring Button")
win.resizable(False, False)
win.geometry("300x200+400+300")


# create a frame from the win
frame = ttk.Frame(win)


def dosomething():
    label.config(text = "Goodbye World")
    btn.config(text = "I have been clicked")


options = {'padx' : 5, "pady":10}

# create the label
label = ttk.Label(frame, text = "Hello World")
label.pack(options)

# create the button
btn = ttk.Button(frame, text = "Click Me", command=dosomething)
btn.pack(options)

# pack the frame
frame.pack(options)

# create the program loop
win.mainloop()