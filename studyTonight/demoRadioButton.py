import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random



win = tk.Tk()
win.title("Radiobutton Demo")
win.geometry("200x200")


def showValue():
    showinfo(title = "Result", message = var.get())

var = tk.StringVar()

lst = list(range(1, 5))

options = {
    "Option A" : str(random.choice(lst)),
    "Option B" : str(random.choice(lst)),
    "Option C" : str(random.choice(lst)),
    "Option D" : str(random.choice(lst))
}


# use for loop to create the radiobutton
for (index, value) in options.items():
    ttk.Radiobutton(win, text = index, variable=var, value = value).pack(side = tk.TOP, ipady = 4)

# add a button here
btn = ttk.Button(win, text = "Get the value", command=showValue)
btn.pack(side = tk.TOP, pady =5, fill = tk.X)


# mainloop of the program
win.mainloop()