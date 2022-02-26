import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2



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
        self.btn1.pack(side = tk.LEFT, expand=True)

        # # button 2
        self.btn2 = ttk.Button(self, text = "Tiger")
        self.btn2['command'] = self.tiger_clicked
        self.btn2.pack(side = tk.LEFT, expand = True)

        # # button 3
        self.btn3 = ttk.Button(self, text = "Tilapia")
        self.btn3['command'] = self.tilapia_clicked
        self.btn3.pack(side = tk.LEFT, expand = True)


        self.pack(side = tk.LEFT, expand = True, anchor = tk.NW)

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


class ImageProcessGray(ttk.Frame):
    def __init__(self, win):
        super().__init__(win)

        # label
        self.label = ttk.Label(self, text="Graying Image")
        self.label.pack(expand=True)

        # image label
        self.imgLabel = ttk.Label(self)
        self.imgLabel.pack(expand=True)

        # button 1
        self.btn1Gray = ttk.Button(self, text="Parrot-Gray")
        self.btn1Gray['command'] = self.parrotGray
        self.btn1Gray.pack(side=tk.LEFT, expand=True)

        # # button 2
        self.btn2Gray = ttk.Button(self, text="Tiger-Gray")
        self.btn2Gray['command'] = self.tigerGray
        self.btn2Gray.pack(side=tk.LEFT, expand=True)

        # # button 3
        self.btn3Gray = ttk.Button(self, text="Tilapia")
        self.btn3Gray['command'] = self.tilapiaGray
        self.btn3Gray.pack(side=tk.LEFT, expand = True)

        self.pack(side=tk.LEFT, expand=True, anchor = tk.NW)

    def parrotGray(self):
        #parrot = Image.open("images/t.png")
        # convert the image to gray
        parrot = cv2.imread("images/parrot.png")
        img_gray = cv2.cvtColor(parrot, cv2.COLOR_BGR2GRAY)

        # convert the image to PIL format
        img_gray = Image.fromarray(img_gray)

        # diplay the image
        img_gray = ImageTk.PhotoImage(img_gray)
        self.imgLabel.config(image=img_gray)
        self.imgLabel.image = img_gray


    def tigerGray(self):
        #parrot = Image.open("images/tiger.png")
        # convert the image to gray
        tiger = cv2.imread("images/tiger.png")
        img_gray = cv2.cvtColor(tiger, cv2.COLOR_BGR2GRAY)

        # convert the image to PIL format
        img_gray = Image.fromarray(img_gray)

        # diplay the image
        img_gray = ImageTk.PhotoImage(img_gray)
        self.imgLabel.config(image=img_gray)
        self.imgLabel.image = img_gray


    def tilapiaGray(self):
        #parrot = Image.open("images/tiger.png")
        # convert the image to gray
        tilapia = cv2.imread("images/tilapia.png")
        img_gray = cv2.cvtColor(tilapia, cv2.COLOR_BGR2GRAY)

        # convert the image to PIL format
        img_gray = Image.fromarray(img_gray)

        # diplay the image
        img_gray = ImageTk.PhotoImage(img_gray)
        self.imgLabel.config(image=img_gray)
        self.imgLabel.image = img_gray


class ImageProcessBlur(ttk.Frame):
    def __init__(self, win):
        super().__init__(win)

        # label
        self.label = ttk.Label(self, text="Blurring Image")
        self.label.pack(expand=True)

        # image label
        self.imgLabel = ttk.Label(self)
        self.imgLabel.pack(expand=True)

        # button 1
        self.btn1Blur = ttk.Button(self, text="Parrot-Blur")
        self.btn1Blur['command'] = self.parrotBlur
        self.btn1Blur.pack(side=tk.LEFT, expand=True)

        # # button 2
        self.btn2Blur = ttk.Button(self, text="Tiger-Gray")
        self.btn2Blur['command'] = self.tigerBlur
        self.btn2Blur.pack(side=tk.LEFT, expand=True)

        # # button 3
        self.btn3Blur = ttk.Button(self, text="Tilapia")
        self.btn3Blur['command'] = self.tilapiaBlur
        self.btn3Blur.pack(side=tk.LEFT, expand = True)

        self.pack(side=tk.LEFT, expand=True, anchor=tk.NW)

    def parrotBlur(self):

        # convert the image to gray
        parrot = cv2.imread("images/parrot.png")

        # convert the image to blur
        img_blur = cv2.medianBlur(parrot, 7)

        # convert the image to PIL format
        img_blur = Image.fromarray(img_blur)

        # diplay the image
        img_blur = ImageTk.PhotoImage(img_blur)
        self.imgLabel.config(image=img_blur)
        self.imgLabel.image = img_blur


    def tigerBlur(self):
        # convert the image to gray
        tiger = cv2.imread("images/tiger.png")

        # convert the image to blur
        img_blur = cv2.medianBlur(tiger, 7)

        # convert the image to PIL format
        img_blur = Image.fromarray(img_blur)

        # diplay the image
        img_blur = ImageTk.PhotoImage(img_blur)
        self.imgLabel.config(image=img_blur)
        self.imgLabel.image = img_blur


    def tilapiaBlur(self):
        # convert the image to gray
        tilapia = cv2.imread("images/tilapia.png")

        # convert the image to blur
        img_blur = cv2.medianBlur(tilapia, 7)

        # convert the image to PIL format
        img_blur = Image.fromarray(img_blur)

        # diplay the image
        img_blur = ImageTk.PhotoImage(img_blur)
        self.imgLabel.config(image=img_blur)
        self.imgLabel.image = img_blur




class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x400")
        self.title("Photo Viewer")
        self.resizable(False, False)

        self.__create_widgets()

    def __create_widgets(self):

        mainframe = MainFrame(self)
        mainframe.pack(expand=True)

        imageprocessgray = ImageProcessGray(self)
        imageprocessgray.pack(expand=True)

        imageprocessblur = ImageProcessBlur(self)
        imageprocessblur.pack(expand = True)




if __name__ == "__main__":
    app = App()
    app.mainloop()
