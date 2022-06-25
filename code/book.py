import tkinter as tk
import tkinter.font as tkFont
import test
from tkinter import messagebox
import tree


class App:
    def __init__(self, root, a, origin, des, dep, day):
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
        GLabel_655["text"] = "車次代號 "
        GLabel_655.place(x=60, y=150, width=100, height=30)

        GLabel_656 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_656['bg'] = '#FAEBD7'
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = str(a)
        GLabel_656.place(x=160, y=150, width=198, height=30)

        '''GLineEdit_391=tk.Entry(root)
        GLineEdit_391["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_391["font"] = ft
        GLineEdit_391["fg"] = "#333333"
        GLineEdit_391["justify"] = "center"
        GLineEdit_391["text"] = "Entry"
        GLineEdit_391.place(x=160,y=150,width=198,height=30)'''

        GLabel_541 = tk.Label(root)
        GLabel_541['bg'] = '#FAEBD7'
        ft = tkFont.Font(family='Times', size=10)
        GLabel_541["font"] = ft
        GLabel_541["fg"] = "#333333"
        GLabel_541["justify"] = "center"
        GLabel_541["text"] = "姓名"
        GLabel_541.place(x=60, y=180, width=100, height=30)

        GLineEdit_309 = tk.Entry(root)
        GLineEdit_309["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_309["font"] = ft
        GLineEdit_309["fg"] = "#333333"
        GLineEdit_309["justify"] = "center"
        GLineEdit_309["text"] = "Entry3"
        GLineEdit_309.place(x=160, y=180, width=198, height=30)

        GLabel_656 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_656['bg'] = '#FAEBD7'
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "電話"
        GLabel_656.place(x=60, y=210, width=100, height=30)

        GLineEdit_392 = tk.Entry(root)
        GLineEdit_392["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_392["font"] = ft
        GLineEdit_392["fg"] = "#333333"
        GLineEdit_392["justify"] = "center"
        GLineEdit_392["text"] = "Entry1"
        GLineEdit_392.place(x=160, y=210, width=198, height=30)

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
        GButton_126.place(x=160, y=242, width=198, height=30)
        GButton_126["command"] = self.GButton_126_command

        GLabel_45 = tk.Label(root)
        GLabel_45['bg'] = '#FAEBD7'
        ft = tkFont.Font(family='Times', size=10)
        GLabel_45["font"] = ft
        GLabel_45["fg"] = "#333333"
        GLabel_45["justify"] = "center"
        GLabel_45["text"] = "訂票"
        GLabel_45.place(x=160, y=120, width=198, height=30)
        self.GLineEdit_309 = GLineEdit_309
        self.GLineEdit_399 = GLineEdit_392
        self.GLineEdit_393 = GLineEdit_393
        self.root = root
        self.a = a
        self.origin = origin
        self.des = des
        self.dep = dep
        self.day = day
        GButton_128 = tk.Button(root)
        GButton_128["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_128["font"] = ft
        GButton_128["fg"] = "#393d49"
        GButton_128["justify"] = "center"
        GButton_128["text"] = "Exit"
        GButton_128.place(x=160, y=270, width=198, height=30)
        GButton_128["command"] = self.GButton_128_command

    def GButton_126_command(self):
        b = self.GLineEdit_309.get()
        c = self.GLineEdit_399.get()
        msg = messagebox.askquestion('My messagebox', '你確定要訂票嗎')
        if msg == 'yes':
            res = test.BookTrain(self.a, b, c, self.origin, self.des, self.dep, self.day)
            if res == 'error':
                messagebox.showerror("My messagebox", "錯誤車次")
                self.root.mainloop()
            else:
                msgs = messagebox.askquestion('My messagebox', '成功訂票! \n是否要查看訂票明細')
                if msgs == 'yes':
                    _, result, column = test.ShowBookings(c)
                    tree.create_treeview(column, result, self.root)
        if msg == 'no':
            self.root.mainloop()

    def GButton_128_command(self):
        self.root.withdraw()
