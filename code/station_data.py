from tkinter import *
from tkinter import ttk
import backend


def create_treeview(win):
    def exit():
        newWindow.withdraw()

    newWindow = Toplevel(win)
    labelExample = Label(newWindow, text="information")
    buttonExample = Button(newWindow, text="exit", command=exit)
    column, result = backend.station_datas()
    tree = ttk.Treeview(newWindow)
    tree["columns"] = column
    for i in column:
        tree.column(i, width=100)

    for i in column:
        tree.heading(i, text=i)

    z = len(result) + 1
    r = []
    for x in result:
        r.append(x)
    r.reverse()
    r1 = tuple(r)
    for x in r1:
        z -= 1
        row = 'No.' + str(z)
        value = []
        for i in x:
            value.append(i)
        tree.insert("", 0, text=row, values=value)
    labelExample.pack()
    tree.pack()
    buttonExample.pack()
