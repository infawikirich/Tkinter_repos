import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

# create the root window
win = tk.Tk()
win.title("Tkinter Yes/No Dialog")
win.geometry("300x150")


# click event handler
def confirm():
    answer = askyesno(title = "confirmation", message = "Are you sure that you want quit?")

    if answer:
        win.destroy()


ttk.Button(
    win,
    text = "Ask Yes/No",
    command = confirm
).pack(expand=True)


win.mainloop()
