from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


# root window
win = tk.Tk()
win.geometry("300x120")
win.title("Progressbar")


def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    if pb['value']