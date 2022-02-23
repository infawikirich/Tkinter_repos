from tkinter import *
from tkinter import ttk



class FeetToMeters:

    def __init__(self, win):
        win.title ("Feet  to Meters")

        mainframe = ttk.Frame(win, padding = "3 3 12 12")
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        win.columnconfigure(0, weight = 1)
        win.rowconfigure(0, weight = 1)


        self.feet = StringVar()
        feetEntry = ttk.Entry(mainframe, width = 7, textvariable = self.feet)
        feetEntry.grid(column = 2, row = 1, sticky = (W, E))

        self.meters = StringVar()
        ttk.Label(mainframe, textvariable = self.meters).grid(column=2, row = 2, sticky = (W, E))
        ttk.Button(mainframe, text = "Calculate", command = self.calculate).grid(column = 3, row = 3, sticky = W)

        ttk.Label(mainframe, text = 'feet').grid(column = 3, row = 1, sticky = E)
        ttk.Label(mainframe, text = "is equivalent to").grid(column = 1, row = 2, sticky = E)
        ttk.Label(mainframe, text = "meters").grid(column = 3, row = 2, sticky = W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)

        feetEntry.focus()
        win.bind("<Return>", self.calculate)


    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass


win = Tk()
FeetToMeters(win)
win.mainloop()