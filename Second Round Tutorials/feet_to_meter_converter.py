from tkinter import *
from tkinter import ttk


# set the up the window
win = Tk()

# set the geometry size
win.geometry("400x200")

# set the title of the window
win.title("Feet to Meters")


# define the calculate command
def calculate(*arg):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# create a frame to hold other widgets
mainframe = ttk.Frame(win, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

# this ensures that the frame expand if the window is resized
win.columnconfigure(0, weight = 1)
win.rowconfigure(0, weight = 1)

# create a variable for the feet
feet = StringVar()

feetEntry = ttk.Entry(mainframe, width = 7, textvariable = feet)
feetEntry.grid(column = 2, row = 1, sticky = (W, E))


# create a variable for the meters
meters = StringVar()
ttk.Label(mainframe, textvariable = meters).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column = 3, row = 3, sticky = W)

ttk.Label(mainframe, text = "feet").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "is equaivalent to").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "meters").grid(column = 3, row = 2, sticky = W)


for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)
    feetEntry.focus()
    win.bind("<Return>", calculate)


# loop for the window
win.mainloop()
