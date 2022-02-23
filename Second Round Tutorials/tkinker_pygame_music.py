import pygame
from tkinter import *
from tkinter import  ttk


# define the function for the sound
def play():
    """This will play the background image when we load or click the playbutton"""
    pygame.mixer.music.load("life.mp3")
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def sound():
    pygame.mixer.Sound.play(sound_effect)


# instantiate the pygame
pygame.init()
sound_effect = pygame.mixer.Sound("crash.wav")

# instatiate tkinter
win = Tk()
win.geometry("180x200")

frame = Frame(win)
frame.pack()

label = ttk.Label(frame, text = "Pygame and Tkinter Mixer")
label.pack()

playBtn = ttk.Button(frame, text = "Play", command = play, width = 15)
playBtn.pack(pady = 5)

soundBtn = ttk.Button(frame, text = "Sound", command = sound, width = 15)
soundBtn.pack(pady = 5)

unpauseBtn = ttk.Button(frame, text = "Unpause", command = unpause, width = 15)
unpauseBtn.pack(pady = 5)

pauseBtn = ttk.Button(frame, text = "Pause", command = pause, width = 15)
pauseBtn.pack(pady = 5)



win.mainloop()