import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo



class MainFrame(ttk.Frame):
    def __init__(self, win):
        super().__init__(win)


        options = {"padx":5, "pady" : 5}


        # label
        self.label = ttk.Label(self, text = "Hello, Jessica Matrins")
        self.label.pack(**options)


        # button
        self.button = ttk.Button(self, text = "Click Me")
        self.button['command'] = self.button_clicked
        self.button.pack(**options)

        # show the frame on the container
        self.pack(**options)

    def button_clicked(self):
        showinfo(title = "Information", message = "Hello, Tkinter")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #configure the root window
        self.title("Frame App")
        self.geometry("300x200")

        self.__create_widgets()

    def __create_widgets(self):
        # create the frame
        frame = MainFrame(self)
        frame.pack(expand=True)


if __name__=="__main__":
    app = App()
    app.mainloop()


