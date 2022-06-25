from tkinter import *
from tkinter import ttk
import book


def create_treeview(column, result, win):
    def select():
        des = tree.selection()
        for de in des:
            a = tree.item(de)['values'][5]
            a= "%04d" % a

            origin=tree.item(de)['values'][1]
            dest = tree.item(de)['values'][3]
            dep = tree.item(de)['values'][7]
            day=(tree.item(de)['values'][10])
            newWindows = Toplevel(newWindow)
            book.App(newWindows, a,origin,dest,dep,day)

    newWindow = Toplevel(win)
    labelExample = Label(newWindow, text="information")
    buttonExample = Button(newWindow, text="booking", command=select)
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
