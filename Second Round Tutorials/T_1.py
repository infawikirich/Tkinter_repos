#!/usr/bin/python3


from tkinter import *

# create the application window
win = Tk()
win.title("Tkinter Window - Center")

window_width = 300
window_height = 200

# get the screen dimension
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# set the position of the window to the center of the screen
win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
win.resizable(False, False)

def select(option):
    print(option)


redButton = Button(win, text = "Red", fg = 'red', command = lambda : select("Red"))
redButton.pack(side = LEFT)

greenButton = Button(win, text = "Black", fg = 'black', command = lambda : select("Black"))
greenButton.pack(side = RIGHT)

blueButton = Button(win, text = "Blue", fg = 'blue', command = lambda : select("Blue"))
blueButton.pack(side = TOP)

blackButton = Button(win, text = "Green", fg = 'red', command = lambda :select("Green"))
blackButton.pack(side = BOTTOM)


#Entering the event main loop
win.mainloop()