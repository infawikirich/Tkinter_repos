from tkinter import *
from tkinter import ttk

win = Tk()


win.geometry("300x300")
win.title("Scrollbar")
win.resizable(0, 0)


# apply the grid layout
win.grid_columnconfigure(0, weight = 1)
win.grid_rowconfigure(0, weight = 1)

# create the text widget
text = Text(win, height = 10)
text.grid(row = 0, column = 0, sticky = EW)


# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(win, orient = 'vertical', command = text.yview)
scrollbar.grid(row = 0, column = 1, sticky = NS)

# communicate back in the scrollbar
text['yscrollcommand'] = scrollbar.set


win.mainloop()