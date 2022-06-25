import tkinter as tk
import tkinter.font as tkFont
import test
import arrtree
import topGUI
from tkinter import messagebox

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
        GLabel_655["text"] = "起始車站代號"
        GLabel_655.place(x=60, y=150, width=100, height=30)

        GLineEdit_391 = tk.Entry(root)
        GLineEdit_391["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_391["font"] = ft
        GLineEdit_391["fg"] = "#333333"
        GLineEdit_391["justify"] = "center"
        GLineEdit_391["text"] = "Entry"
        GLineEdit_391.place(x=160, y=150, width=198, height=30)

        GLabel_541 = tk.Label(root)
        GLabel_541['bg'] = '#FAEBD7'
        ft = tkFont.Font(family='Times', size=10)
        GLabel_541["font"] = ft
        GLabel_541["fg"] = "#333333"
        GLabel_541["justify"] = "center"
        GLabel_541["text"] = "終點車站代號"
        GLabel_541.place(x=60, y=180, width=100, height=30)

        GLineEdit_303 = tk.Entry(root)
        GLineEdit_303["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_303["font"] = ft
        GLineEdit_303["fg"] = "#333333"
        GLineEdit_303["justify"] = "center"
        GLineEdit_303["text"] = "Entry3"
        GLineEdit_303.place(x=160, y=180, width=198, height=30)

        GLabel_656 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_656['bg'] = '#FAEBD7'
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "出發時間"
        GLabel_656.place(x=60, y=210, width=100, height=30)

        GLineEdit_392 = tk.Entry(root)
        GLineEdit_392["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_392["font"] = ft
        GLineEdit_392["fg"] = "#333333"
        GLineEdit_392["justify"] = "center"
        GLineEdit_392["text"] = "Entry1"
        GLineEdit_392.place(x=160, y=210, width=198, height=30)

        GLabel_657 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_657['bg'] = '#FAEBD7'
        GLabel_657["font"] = ft
        GLabel_657["fg"] = "#333333"
        GLabel_657["justify"] = "center"
        GLabel_657["text"] = "抵達時間"
        GLabel_657.place(x=60, y=240, width=100, height=30)

        GLineEdit_393 = tk.Entry(root)
        GLineEdit_393["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_393["font"] = ft
        GLineEdit_393["fg"] = "#333333"
        GLineEdit_393["justify"] = "center"
        GLineEdit_393["text"] = "Entry2"
        GLineEdit_393.place(x=160, y=240, width=198, height=30)

        GButton_126 = tk.Button(root)
        GButton_126["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_126["font"] = ft
        GButton_126["fg"] = "#393d49"
        GButton_126["justify"] = "center"
        GButton_126["text"] = "OK"
        GButton_126.place(x=160, y=300, width=200, height=30)
        GButton_126["command"] = self.GButton_126_command

        GLabel_45 = tk.Label(root)
        GLabel_45['bg'] = '#FAEBD7'
        ft = tkFont.Font(family='Times', size=10)
        GLabel_45["font"] = ft
        GLabel_45["fg"] = "#333333"
        GLabel_45["justify"] = "center"
        GLabel_45["text"] = "查詢車站代號"
        GLabel_45.place(x=160, y=120, width=198, height=30)

        GButton_128 = tk.Button(root)
        GButton_128["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_128["font"] = ft
        GButton_128["fg"] = "#393d49"
        GButton_128["justify"] = "center"
        GButton_128["text"] = "Exit"
        GButton_128.place(x=160, y=328, width=200, height=30)
        GButton_128["command"] = self.GButton_128_command

        GLabel_658 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_658['bg'] = '#FAEBD7'
        GLabel_658["font"] = ft
        GLabel_658["fg"] = "#333333"
        GLabel_658["justify"] = "center"
        GLabel_658["text"] = "yyyy-mm-dd"
        GLabel_658.place(x=60, y=270, width=100, height=30)

        GLineEdit_394 = tk.Entry(root)
        GLineEdit_394["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_394["font"] = ft
        GLineEdit_394["fg"] = "#333333"
        GLineEdit_394["justify"] = "center"
        GLineEdit_394["text"] = "Entry4"
        GLineEdit_394.place(x=160, y=270, width=198, height=30)
        self.GLineEdit_391 = GLineEdit_391
        self.GLineEdit_303 = GLineEdit_303
        self.GLineEdit_392 = GLineEdit_392
        self.GLineEdit_393 = GLineEdit_393
        self.root = root
        self.GLineEdit_394=GLineEdit_394

    def GButton_126_command(self):
        a = self.GLineEdit_391.get()
        b = self.GLineEdit_303.get()
        c = self.GLineEdit_392.get()
        c = '"' + c + '"'
        d = self.GLineEdit_393.get()
        d = '"' + d + '"'
        e = self.GLineEdit_394.get()
        e = '"' + e + '"'
        t,column, result = test.AvailableTrains(a, b, c, d,e)
        if t == 'error':
            messagebox.showerror("My messagebox", "錯誤")
            self.root.mainloop()
        else:
            arrtree.create_treeview(column, result, self.root)

    def GButton_128_command(self):
        self.root.withdraw()
        newWindow = tk.Toplevel(self.root)
        topGUI.App(newWindow)
