import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING


# create the root window
win = tk.Tk()
win.title("Tkinter Ok/Cancel Dialog")
win.geometry("300x150")


# create event handler
def confirm():
    answer = askokcancel(
        title = "Confirmation",
        message="Deleting will delete all the data",
        icon = WARNING
    )
    
    if answer:
        showinfo(
            title = "Deleting Status",
            message="The data is deleted successfully"
        )


ttk.Button(win, text = "Delete All", command = confirm).pack(expand = True)

# start the app
win.mainloop()
