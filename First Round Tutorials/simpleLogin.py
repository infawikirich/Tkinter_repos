from tkinter import *
from tkinter import messagebox


# create in instance
class Window(Tk):
    def __init__(self):
        super().__init__()

        self.intro_text = StringVar()
        self.name_text = StringVar()
        self.password_text = StringVar()

        # set a welcoming address
        self.intro_text.set('Welcome to my humble Tkinter login')
        self.label = Label(self, text=self.intro_text.get())
        self.label.place(x = 20, y = 80, relwidth = 0.9)

        # takes  user's name
        self.name_label = Label(self, text='Full name :')
        self.name_label.place( x= 0, y = 150, width = 150, bordermode = OUTSIDE)
        self.name_entry = Entry(self, textvar=self.name_text)
        self.name_entry.place(x = 110, y = 150, width = 170)

        # takes  user password
        self.password_label = Label(self, text='Password :')
        self.password_label.place(x=0, y=200, width=150, bordermode = OUTSIDE)
        self.password_entry = Entry(self, textvar = self.password_text, show = '*')
        self.password_entry.place(x = 110, y = 200, width = 170)

        # create a button
        self.btn = Button(self, text='Login', command = self.login)
        self.btn.place(x = 50, y = 230)

    def display(self):
        message = 'Welcome ' + self.name_entry.get() + '\n you have successfully login '
        return message

    def login(self):
        password = '12345'
        if self.password_entry.get() == password:
            messagebox.showinfo('Login', self.display())
            self.intro_text.set('This dialog is self destructive in 2 second ' + self.name_entry.get())
            self.after(2000, self.destroy)
        else:
            messagebox.showerror('Error', 'Incorrect Password')


if __name__ == '__main__':
    window = Window()
    window.title('Password')
    window.geometry('300x300')
    window.mainloop()
