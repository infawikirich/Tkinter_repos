import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


win = tk.Tk()
win.title("Treeview")
win.geometry("620x200")

# define columns
columns = ("first_name", "last_name", "email")

tree = ttk.Treeview(win, columns=columns, show = "headings")

# define headings
tree.heading("first_name", text = "First_name")
tree.heading("last_name", text = "Last Name")
tree.heading("email", text = "Email")

# add data to the treeview
contacts = []
for n in range(1, 100):
    contacts.append((f"frist {n}", f"last {n}", f"email{n}vispad.com"))

# add data to three view
for contact in contacts:
    tree.insert("", tk.END, values = contact)

def item_selected