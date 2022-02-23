from tkinter import *
from tkinter import ttk
from ctypes import windll

win = Tk()
win.geometry("600x400+300+50")
win.resizable(False, False)
win.attributes('-topmost', 1)
win.iconbitmap("icon.ico")
win.title("Tkinter Tutorials")


frame = ttk.Frame(win, padding = (3, 3, 12, 12))
mainframe = ttk.Frame(frame, borderwidth = 5, relief = "ridge", width = 200, height = 100)
nameLabel = ttk.Label(frame, text = 'Name')
nameEntry = ttk.Entry(frame)


oneVar = BooleanVar(value = True)
twoVar = BooleanVar(value = False)
threeVar = BooleanVar(value = True)

one = ttk.Checkbutton(frame, text = "One", variable = oneVar, onvalue = True)
two = ttk.Checkbutton(frame, text = "Two", variable = twoVar, onvalue = True)
three = ttk.Checkbutton(frame, text = "Three", variable = threeVar, onvalue = True)

okbtn = ttk.Button(frame, text = "Okay")
cancelbtn = ttk.Button(frame, text = "Cancel")


# layout the widget on the screen
mainframe.grid(column = 0, row = 0, sticky = (N, S,E, W))
frame.grid(column = 0, row = 0, columnspan = 3, rowspan = 2, sticky = (N, S, E,W))
nameLabel.grid(column = 3, row = 0, columnspan = 2, sticky = (N, W), padx = 5)
nameEntry.grid(column = 3, row = 1, columnspan = 2, sticky = (N, E, W), pady = 5, padx = 5)
one.grid(column = 0, row = 3)
two.grid(column = 1, row = 3)
three.grid(column = 2, row = 3)
okbtn.grid(column = 3, row = 3)
cancelbtn.grid(column = 4, row = 3)

win.columnconfigure(0, weight = 1)
win.rowconfigure(0, weight = 1)
mainframe.columnconfigure(0, weight = 3)
mainframe.columnconfigure(1, weight = 3)
mainframe.columnconfigure(2, weight = 3)
mainframe.columnconfigure(3, weight = 1)
mainframe.columnconfigure(4, weight = 1)
mainframe.rowconfigure(1, weight = 1)


win.mainloop()


