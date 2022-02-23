#!/usr/bin/python3


from tkinter import *
from functools import partial
from tkinter import messagebox




def call_result(n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) + int(num2)
    messagebox.showinfo('Result = %s' , result)

    return

root = Tk()
root.geometry('400x200+100+200')

root.title('Simple Calculator')

# define variable type
number1 = StringVar()
number2 = StringVar()

labelNum1 = Label(root, text = 'A').grid(row=1, column=0)
labelNum2 = Label(root, text = 'B').grid(row = 2, column=0)

labelResult = Label(root).grid(row = 7, column = 2)

entry_1 = Entry(root, textvariable = number1).grid(row =1 , column=2)
entry_2 = Entry(root, textvariable = number2).grid(row = 2 , column=2)

call_result = partial(call_result, number1, number2)

buttonCal = Button(root, text = "Calculate", command = call_result).grid(row=3, column =0 )



root.mainloop()