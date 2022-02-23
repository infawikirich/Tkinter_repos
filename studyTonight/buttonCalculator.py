import tkinter as tk
from tkinter.messagebox import showinfo


# create the base root
win = tk.Tk()
win.title("Button Calculator")
win.geometry("215x320")
win.resizable(False, False)


def click():
    showinfo("A button has been clicked")



# use for loop to create 9 buttons
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            win,
            relief= tk.RAISED,
            borderwidth= 1
        )

        frame.grid(row = i, column = j, padx = 2, pady = 2)
        btn = tk.Button(frame, text = f"{j}", padx = 25, pady = 25, command = click)
        btn.pack(expand=True )


# the loop of the game
win.mainloop()

