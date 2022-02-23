import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# create the root window
win = tk.Tk()
win.geometry("200x100")
win.resizable(False, False)
win.title("List box")

win.columnconfigure(0, weight = 1)
win.rowconfigure(0, weight = 1)

# create a list box
langs = ("Java", "C#", "C", "C++", "Python", "Go", "JavaScript", "PHP", "Swift")

langs_var = tk.StringVar(value = langs)

listbox = tk.Listbox(win, listvariable = langs_var, height = 3, selectmode = "extended")
listbox.grid(column = 0, row = 0, sticky = 'nwes')

scrollbar = ttk.Scrollbar(win, orient = 'vertical', command = listbox.yview)

listbox['yscrollcommand'] = scrollbar.set


# handle event
def items_selected(event):
    """handle item selected event"""

    # get selected indices
    selected_indices = listbox.curselection()

    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f"You selected :{selected_langs}"

    showinfo(title = "Information", message=msg)


listbox.bind("<<ListBoxSelect>>", items_selected)


win.mainloop()