from tkinter import *
from tkinter import ttk


# instantiate tkinter
win = Tk()

win.geometry("200x200")

def var_states():
    print("male: %d, \nfemale: %d" %(var1.get(), var2.get()))


ttk.Label(win, text = "Your sex:").grid(row = 0, sticky = W)

var1  = IntVar()
ttk.Checkbutton(win, text = "male", variable = var1).grid(row = 1, sticky = W)

var2  = IntVar()
ttk.Checkbutton(win, text = "female", variable = var2).grid(row = 2, sticky = W)

ttk.Button(win, text = "Quit", command = win.quit).grid(row =3, sticky = W, pady = 4 )
ttk.Button(win, text = "Show", command = var_states).grid(row =4, sticky = W, pady = 4 )

win.mainloop()



