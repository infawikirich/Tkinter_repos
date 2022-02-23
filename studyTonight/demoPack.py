"""
This program about the pack() geometry manager thats
puts object as default in the same order which they are assigned to the
window
"""

import tkinter as tk


# create a base window
win = tk.Tk()
win.title("Pack Geometry Manager Default")
win.geometry("300x300")
#win.resizable(False, False)


# add a frame to the root windwo
# Frames are used to hold other widgets
frame1 = tk.Frame(win, width = 100, height = 100, bg = "orange")
frame1.pack(fill = tk.X)

frame2 = tk.Frame(win, width = 50, height = 50, bg = "blue")
frame2.pack(fill = tk.X)

frame3 = tk.Frame(win, width = 25, height = 25, bg = "green")
frame3.pack(fill = tk.X)







# the mainloop of the program
win.mainloop()