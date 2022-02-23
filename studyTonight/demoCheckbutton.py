import tkinter as tk
from tkinter.messagebox import showinfo


win = tk.Tk()
win.geometry("300x300")


label = tk.Label(win, text = "Vispad Institute of Technology", fg = 'blue', font = '100')
label.pack()

# create variables for
checkbtn1 = tk.IntVar()
checkbtn2 = tk.IntVar()
checkbtn3 = tk.IntVar()

def checkBtn1Func():
    showinfo(title = "Result", message=checkbtn1.get())

def checkBtn2Func():
    showinfo(title = "Result", message=checkbtn2.get())

def checkBtn3Func():
    showinfo(title = "Result", message=checkbtn3.get())


btn1 = tk.Checkbutton(win, text = " Python Programming", command=checkBtn1Func,
                      variable=checkbtn1, onvalue=1,offvalue=0, height=2, width=20)

btn2 = tk.Checkbutton(win, text = " Computational Modelling", command = checkBtn2Func,
                      variable=checkbtn2, onvalue=1,offvalue=0, height=2, width=20)

btn3 = tk.Checkbutton(win, text = " 3D modelling", command= checkBtn3Func,
                      variable=checkbtn3, onvalue=1,offvalue=0, height=2, width=10)



btn1.pack()
btn2.pack()
btn3.pack()






win.mainloop()