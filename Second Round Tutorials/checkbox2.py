import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo



win = tk.Tk()
win.geometry("300x200")
win.resizable(False, False)
win.title("Checkbox Demo")


agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title = "Result", message = agreement.get())


ttk.Checkbutton(win, text = "I agree", command = agreement_changed, variable = agreement, onvalue = 'agree',
                offvalue = 'disagree').pack()



win.mainloop()
