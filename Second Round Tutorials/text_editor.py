from tkinter import *
from tkinter import ttk


win = Tk()

win.geometry("300x300")
win.resizable(0,0)
win.title("Text Editor")


text = Text(win, height = 8)
text.pack()
text.insert("1.0", "This is a text widget demo")
text_content = text.get("1.0", 'end')
text['state'] = 'disabled'


win.mainloop()