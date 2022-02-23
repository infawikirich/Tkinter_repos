import tkinter as tk
from tkinter import ttk


# root window
win = tk.Tk()
win.geometry('300x200')
win.resizable(False, False)
win.title("Slider Demo")


win.columnconfigure(0, weight = 1)
win.columnconfigure(1, weight = 3)

# slider current value
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text = get_current_value())

# label for the slider
slider_label = ttk.Label(win, text = "Slider")
slider_label.grid(column = 0, row = 0, sticky = 'w')

# slider
slider = ttk.Scale(win, from_ = 0, to = 100, orient = 'horizontal', command = slider_changed, variable = current_value)
slider.grid(column =1 , row = 0, sticky = 'we')

# current value label
current_value_label = ttk.Label(win, text = "Current Value")
current_value_label.grid(row = 1, columnspan = 2, sticky = 'n', ipadx = 10, ipady = 10)

# value label
value_label = ttk.Label(win, text = get_current_value())
value_label.grid(row = 2, columnspan = 2, sticky = 'n')


win.mainloop()

