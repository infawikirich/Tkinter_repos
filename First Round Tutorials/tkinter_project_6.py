import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # create an instance of the text variable
        self.label_text = tk.StringVar()
        self.label_text.set('My name is :')

        self.name_text = tk.StringVar()

        self.label = tk.Label(self, text = self.label_text.get())
        self.label.pack(fill = tk.BOTH, expand = 1, padx = 100, pady = 30)

        self.name_entry = tk.Entry(self, textvar = self.name_text)
        self.name_entry.pack(fill = tk.BOTH, expand = 1, padx = 20, pady = 20)

        self.hello_button = tk.Button(self, text = 'Say Hello', command=self.say_hello)
        self.hello_button.pack(side = tk.LEFT, padx = (20, 0), pady =(0, 20))

        self.goodbye_button = tk.Button(self, text = "Say Goodbye",command = self.say_goodbye)
        self.goodbye_button.pack(side = tk.RIGHT, padx = (0, 20), pady = (0, 20))


    # define method for the calback function
    def say_hello(self):
        message = "Hello there \n" + self.name_entry.get()
        messagebox.showinfo('Hello', message)

    def say_goodbye(self):
        if messagebox.askyesno("Close Window?", "Would you like to close this window?"):
            self.label_text.set('Window will close in 2 second')
            self.after(2000, self.destroy)
        else:
            messagebox.showinfo("Not Closing", "Great ! This window will stay open")

if __name__ == '__main__':
    window = Window()
    window.title('My Tkinter App')
    window.geometry('300x200')
    window.mainloop()