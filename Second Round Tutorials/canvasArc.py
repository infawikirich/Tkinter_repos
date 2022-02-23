#!/urs/bin/python3


from tkinter import *


win = Tk()



win.geometry("400x400")


canvas = Canvas(win, bg = "lightgreen", width = 400, height = 400)

# create object on the canvas
canvas.create_arc((50, 70, 250, 300), start = 50, extent = 300, fill = "red")

canvas.pack()


win.mainloop()
