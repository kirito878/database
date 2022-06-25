import tkinter as tk
import tkinter.font as tkFont
import test
import tree
from tkinter import messagebox
import topGUI

class App:
    def __init__(self, root):
        # setting title
        root.title("ticket")
        back = tk.PhotoImage(file='0.gif')
        self.img = back
        b = tk.Label(root, image=self.img, bd=0)
        b.pack()
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.config(bg="#FAEBD7")
        root.resizable(width=False, height=False)

        GLabel_655 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_655['bg'] = '#FAEBD7'
        GLabel_655["font"] = ft
        GLabel_655["fg"] = "#333333"
        GLabel_655["justify"] = "center"
        GLabel_655["text"] = "電話"
        GLabel_655.place(x=60, y=150, width=100, height=30)

        GLineEdit_391 = tk.Entry(root)
        GLineEdit_391["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_391["font"] = ft
        GLineEdit_391["fg"] = "#333333"
        GLineEdit_391["justify"] = "center"
        GLineEdit_391["text"] = "Entry11"
        GLineEdit_391.place(x=160, y=150, width=198, height=30)
        GButton_126 = tk.Button(root)
        GButton_126["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_126["font"] = ft
        GButton_126["fg"] = "#393d49"
        GButton_126["justify"] = "center"
        GButton_126["text"] = "OK"
        GButton_126.place(x=161, y=180, width=199, height=30)
        GButton_126["command"] = self.GButton_126_command

        GLabel_45 = tk.Label(root)
        GLabel_45['bg'] = '#FAEBD7'
        ft = tkFont.Font(family='Times', size=10)
        GLabel_45["font"] = ft
        GLabel_45["fg"] = "#333333"
        GLabel_45["justify"] = "center"
        GLabel_45["text"] = "查票"
        GLabel_45.place(x=160, y=120, width=198, height=30)
        self.GLineEdit_391 = GLineEdit_391
        self.root = root
        GButton_127 = tk.Button(root)
        GButton_127["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_127["font"] = ft
        GButton_127["fg"] = "#393d49"
        GButton_127["justify"] = "center"
        GButton_127["text"] = "Exit"
        GButton_127.place(x=161, y=208, width=199, height=30)
        GButton_127["command"] = self.GButton_127_command

    def GButton_126_command(self):
        a = self.GLineEdit_391.get()
        t,result, column = test.ShowBookings(a)
        if t == 'error':
            messagebox.showerror("My messagebox", "查無此電話")
            self.root.mainloop()
        else:
            tree.create_treeview(column, result, self.root)
    def GButton_127_command(self):
        self.root.withdraw()
        newWindow = tk.Toplevel(self.root)
        topGUI.App(newWindow)

