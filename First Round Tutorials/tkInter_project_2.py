#!/usr/bin/python3

from tkinter import *

parent = Tk()

parent.geometry('200x600')

def hello():
    print('hello!')

def select():
    sel = "Value = " + str(v.get())
    label.config(text = sel)


# create a toplevel menu
menubar = Menu(parent)
menubar.add_command(label = 'Hello!', command = hello)
menubar.add_command(label = 'Quit!', command = parent.quit)

# display the menu
parent.config(menu = menubar)

# Add a message here
var = StringVar()
msg = Message(parent, text = 'Welcome to Vision Institute')
msg.pack()


label = Label(parent, text = "A list of favourite countries...")
label.pack()

listbox = Listbox(parent)
listbox.insert(1, 'India')
listbox.insert(2, 'USA')
listbox.insert(3, 'Japan')
listbox.insert(4, 'Australia')
listbox.pack()

#this button will delete the selected item from the list
btn = Button(parent, text='delete!', command = lambda listbox = listbox : listbox.delete(ANCHOR))
btn.pack()


v = DoubleVar()
scale = Scale(parent, variable = v, from_ = 1, to = 50, orient = HORIZONTAL)
scale.pack(anchor = CENTER)

btn1 = Button(parent, text = 'Value', command = select)
btn1.pack(anchor = CENTER)

label = Label(parent)
label.pack()

sb = Scrollbar(parent)
sb.pack(side = RIGHT, fill = Y)

mylist = Listbox(parent, yscrollcommand = sb.set)
for line in range(30):
    mylist.insert(END, "Number" + str(line))

mylist.pack(side = LEFT)
sb.config(command = mylist.yview)

parent.mainloop()