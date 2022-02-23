import  tkinter as tk




# create a root window
win = tk.Tk()
win.title("Label of window")
win.geometry("300x300+200+200")
win.resizable(False, False)


# create a variable
var = tk.StringVar()
label = tk.Label(win, textvariable = var, relief = tk.RAISED, bg = "red", fg = "white")

# set the label value
var.set("Hey!? Welcome to Vispad Institue of Technology")

label.pack(expand = True)



# mainloop of the program
win.mainloop()

