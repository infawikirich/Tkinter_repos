import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# create the frame
class MainFrame(ttk.Frame):
    def __init__(self, win):
        super().__init__(win)

        # label
        self.label = ttk.Label(self, text="Welcome to my Animals Image Viewer")
        self.label.pack(expand=True)

        # image label
        self.imgLabel = ttk.Label(self)
        self.imgLabel.pack(expand = True)


        # button 1
        self.btn1 = ttk.Button(self, text="Parrot")
        self.btn1['command'] = self.parrot_clicked
        self.btn1.pack(expand=True)

        # # button 2
        self.btn2 = ttk.Button(self, text = "Tiger")
        self.btn2['command'] = self.tiger_clicked
        self.btn2.pack(expand = True)

        # # button 3
        self.btn3 = ttk.Button(self, text = "Tilapia")
        self.btn3['command'] = self.tilapia_clicked
        self.btn3.pack(expand = True)

        self.pack(expand = True)

    def parrot_clicked(self):
        parrot = Image.open("images/parrot.png")
        render = ImageTk.PhotoImage(parrot)
        self.imgLabel.config(image = render)
        self.imgLabel.image = render

    def tiger_clicked(self):
        parrot = Image.open("images/tiger.png")
        render = ImageTk.PhotoImage(parrot)
        self.imgLabel.config(image=render)
        self.imgLabel.image = render

    def tilapia_clicked(self):
        parrot = Image.open("images/tilapia.png")
        render = ImageTk.PhotoImage(parrot)
        self.imgLabel.config(image=render)
        self.imgLabel.image = render



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("Photo Viewer")
        self.resizable(False, False)

        self.__create_widgets()

    def __create_widgets(self):
        frame = MainFrame(self)
        frame.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
