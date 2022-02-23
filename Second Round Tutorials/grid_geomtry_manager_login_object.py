import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("240x100")
        self.title("Geometry Management")
        self.resizable(0, 0)


        # configure the grid
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 3)
        self.columnconfigure(2, weight = 2)

        self.create_widgets()


    def create_widgets(self):
        # username
        nameLabel = ttk.Label(self, text = "Username :")
        nameLabel.grid(column = 0, row = 0, sticky = tk.W, padx = 5, pady = 5)


        nameEntry = ttk.Entry(self)
        nameEntry.grid(column =1, row = 0, sticky = tk.E, padx = 5, pady = 5, columnspan = 3)


        # password
        pswdLabel = ttk.Label(self, text = "Password :")
        pswdLabel.grid(column = 0, row = 1, sticky = tk.W, padx = 5, pady = 5)

        pswdEntry = ttk.Entry(self, show = "*")
        pswdEntry.grid(column = 1, row = 1, sticky = tk.E, padx = 5, pady = 5, columnspan = 3)


        # login button
        loginBtn = ttk.Button(self, text = "Login")
        loginBtn.grid(column = 2, row = 3, sticky = tk.E, padx = 5, pady = 5)



if __name__ == "__main__":
    app = App()
    app.mainloop()
