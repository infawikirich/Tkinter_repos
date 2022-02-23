import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo



win = tk.Tk()
win.geometry("300x300")
win.title("Radio Button Demo")
win.resizable(False, False)


def show_selected_size():
    showinfo(title = "Result", message = selected_size.get())


selected_size = tk.StringVar()
sizes = (("Small", "S"),
         ("Medium", "M"),
         ("Large", "L"),
         ("Extra Large", "XL"),
         ("Extra Extra Large", "XXL"))


# Label
label = ttk.Label(text = "What's your t-shirt size?")
label.pack(fill = 'x', padx = 5, pady = 5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(win, text = size[0], value = size[1], variable = selected_size)

    r.pack(fill = 'x', padx = 5, pady = 5)



button = ttk.Button(win, text = "Get Selected Size", command = show_selected_size)
button.pack(fill = 'x', padx = 5, pady = 5)

win.mainloop()