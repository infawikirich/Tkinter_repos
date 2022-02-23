import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo


# creeate the root window
win = tk.Tk()
win.title("Tkinter OK/Retry Dialog")
win.geometry("300x150")


# click event handler
def confirm():
    answer = askretrycancel(
        title = "Connection Issue",
        message = "The database server is unreachable. Do you want to retry?"

    )
    if answer:
        showinfo(
            title = "Information",
            message="Attempt to connect to the database again"
        )

ttk.Button(
    win,
    text = "Connect to the Database Server",
    command=confirm
).pack(expand=True)

win.mainloop()

