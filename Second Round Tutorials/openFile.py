import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


# create the root window
win = tk.Tk()
win.title("Tkinter Open File Dialog")
win.resizable(False, False)
win.geometry("300x150")


def select_file():
    filetypes = (
        ("text files", "*.txt"),
        ("All files", "*.*")
    )

    filename = fd.askopenfilenames(
        title = "Open file",
        initialdir="/",
        filetypes = filetypes
    )

    showinfo(
        title = "Selected File",
        message = filename
    )

# Open button
open_button = ttk.Button(
    win,
    text = "Open a File",
    command = select_file
)

open_button.pack(expand = True)


# run the application
win.mainloop()