import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning


# create the root window
win = tk.Tk()
win.title("Tkinter MessageBox")
win.resizable(False, False)
win.geometry("300x150")


options = {"fill": "both", 'padx':10, 'pady': 10, 'ipadx':5}

ttk.Button(
    win,
    text = "Show an error message",
    command = lambda : showerror(
        title = "Error",
        message = "This is an error message"
    )
).pack(**options)



ttk.Button(
    win,
    text = "Show an warning message",

    command = lambda : showwarning(
        title = "Warning",
        message="This is a warning message"
    )
).pack(**options)



ttk.Button(
    win,
    text = "Show an information message",
    command = lambda : showinfo(
        title = "Information",
        message = "This is an information message"
    )
).pack(**options)


# run the app
win.mainloop()