from tkinter import  *
from tkinter import ttk


class Checkbar(Frame):
    def __init__(self, parent = None, picks = [], side = LEFT, anchor = W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text = pick, variable = var)
            chk.pack(side = side, anchor = anchor, expand = YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()),self.vars)


if __name__ == "__main__":
    win = Tk()
    lng = Checkbar(win, ['Python', 'Ruby', 'Perl', 'C++'])
    tgl = Checkbar(win, ['English', 'German'])
    lng.pack(side = TOP, fill = X)
    tgl.pack(side = LEFT)
    lng.config(relief = GROOVE, bd = 2)


    def allstates():
        print(list(lng.state()), list(tgl.state()))
    Button(win, text = "Quit", command = win.quit).pack(side = RIGHT)
    Button(win, text = "Peek", command = allstates).pack(side = RIGHT)

    win.mainloop()
