from tkinter import *


root = Tk()

root.geometry('200x200')
root.resizable(0,0)
root.title('tkInter Tutorial')

def open():
    top = Toplevel(root)
    top.mainloop()

spin = Spinbox(root, from_=0, to = 25)
spin.place(x = 20, y = 20)

btn = Button(root, text = 'Open', command = open)
btn.place(x=75, y = 50)


root.mainloop()