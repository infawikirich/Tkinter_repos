import tkinter as tk
from tkinter.messagebox import showinfo


# set the root window
win = tk.Tk()
win.title("Button Demo")
win.geometry("200x200")
win.resizable(False, False)

def click():
    showinfo("Wooow I have been clicked")




labelTitle = tk.Label(win, text = "This is a button Tutorials \n I am trying my way out\n I am using the pack manager",
                 bg = "red", fg = "White", pady = 5, font = "times")
labelTitle.pack(fill = tk.X)

btn = tk.Button(win, text = "click me", command = click)
btn.pack(side=tk.TOP)






win.mainloop()




