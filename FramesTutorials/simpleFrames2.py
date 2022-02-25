import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# create the frame
class MainFrame(ttk.Frame):
  def __init__(self, win):
    super().__init__(win)
    
    # label
    self.label = ttk.Label(self, text = "Welcome to my Animals Image Viewer")
    self.label.grid(row = 0, column = 0)
    
    # button 1
    self.btn1 = ttk.Button(self, text = "Parrot")
    self.btn1['command'] = self.parrot_clicked
    self.btn1.grid(row = 1, column = 0)
    
    # button 2
    self.btn2 = ttk.Button(self, text = "Tiger")
    self.btn2['command'] = self.tiger_clicked
    self.btn2.grid(row = 1, column = 1)
    
    # button 3
    self.btn3 = ttk.Button(self, text = "Tilapia")
    self.btn3['command'] = self.tilapia_clicked
    self.btn3.grid(row = 1, column = 2)
    
    
  def parrotImg(self):
    load = Image.open
    
