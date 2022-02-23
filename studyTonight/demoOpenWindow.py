import tkinter as tk


# create a base window
win = tk.Tk()
win.title("Simple Tkinter Demo")
win.geometry("300x300+100+100")
win.resizable(False, False)


label = tk.Label(win, text = "Hello, Welcome to Vispad Institute of Technology")
label.pack(expand = True)







# mainloop for the program to run
win.mainloop()