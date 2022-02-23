from tkinter import *
from tkinter import messagebox


class Window(Tk):
    def __init__(self):
        super().__init__()

        # define variables
        self.intro_text = StringVar()
        self.ans_text = StringVar()
        self.num_1 = StringVar()
        self.num_2 = StringVar()

        self.intro_text.set('This is a simple Calculator. Input the number and \n click on the sign to perform the calculation')
        self.intro_label = Label(self, text = self.intro_text.get())
        self.intro_label.place(x = 5, y = 5, relwidth = 0.9)

        self.entry_num1 = Entry(self, textvar = self.num_1)
        self.entry_num1.place(x = 100, y = 70, width = 50)

        self.entry_num2 = Entry(self, textvar=self.num_2)
        self.entry_num2.place(x = 200, y = 70, width = 50)

        self.ans_text.set('Waiting for you to press a button')
        self.ans_label = Label(self, text=self.ans_text.get())
        self.ans_label.place(x = 0, y = 120, relwidth = 0.9)


        self.plus_btn = Button(self, text = ' + ', bg = 'red', fg = 'white', command = self.add)
        self.plus_btn.place(x = 5, y = 170, width = 50)

        self.minus_btn = Button(self, text = ' - ', bg = 'blue', fg = 'white', command = self.minus)
        self.minus_btn.place(x = 100, y = 170, width = 50)

        self.multiply_btn = Button(self, text = 'x', bg = 'red', fg = 'white', command = self.multiply)
        self.multiply_btn.place(x = 200, y = 170, width = 50)

        self.divide_btn = Button(self, text = " / ", bg = 'blue', fg = 'white', command = self.divide)
        self.divide_btn.place(x = 300, y = 170, width = 50)



    def add(self):
        number_1 = self.entry_num1.get()
        number_2 = self.entry_num2.get()
        result = float(number_1) + float(number_2)
        messagebox.showinfo('Answer', result)


    def minus(self):
        number_1 = self.entry_num1.get()
        number_2 = self.entry_num2.get()
        result = float(number_1) - float(number_2)
        messagebox.showinfo('Answer', result)


    def multiply(self):
        number_1 = self.entry_num1.get()
        number_2 = self.entry_num2.get()
        result = float(number_1) * float(number_2)
        messagebox.showinfo('Answer', result)

    def divide(self):
        number_1 = self.entry_num1.get()
        number_2 = self.entry_num2.get()
        result = float(number_1) / float(number_2)
        messagebox.showinfo('Answer', result)



if __name__ == "__main__":
    window = Window()
    window.title('Simple Calculator')
    window.geometry('400x400')
    window.resizable(0,0)
    window.mainloop()
