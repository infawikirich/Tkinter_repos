import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo



# create the root window
win = tk.Tk()
win.geometry("200x400")
win.title("RadioButton with Roman numerals")
win.resizable(False, False)


# create a variable to keep track of the radiobutton
var = tk.StringVar()

# create a call back function
def showValue():
    showinfo(title = "Result", message = var.get())


# create the a dictionary of numbers with roman numerals
nums = {
    "1" : "I",
    "2" : "II",
    "3" : "III",
    "4" : "IV",
    "5" : "V",
    "6" : "VI",
    "7" : "VII",
    "8" : "VIII",
    "9" : "IX",
    "10" : "X"
}


# use for loop to draw the radio button the windows
for (index, value) in nums.items():
    ttk.Radiobutton(win, text = index, variable=var, value = value).pack(side = tk.TOP, pady = 5)


#create a button
btn = ttk.Button(win, text = "Get the Roman Numeral Value", command=showValue)
btn.pack(fill = tk.X)



# mainloop
win.mainloop()