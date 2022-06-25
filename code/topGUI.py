import tkinter as tk
import tkinter.font as tkFont
import searchbook
import station_data
import avtrain


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
        root.resizable(width=False, height=False)
        root.config(bg="#FAEBD7")
        GButton_985 = tk.Button(root)
        GButton_985["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_985["font"] = ft
        GButton_985["fg"] = "#000000"
        GButton_985["justify"] = "center"
        GButton_985["text"] = "查票"
        GButton_985.place(x=180, y=190, width=70, height=25)
        GButton_985["command"] = self.GButton_985_command

        GButton_545 = tk.Button(root)
        GButton_545["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_545["font"] = ft
        GButton_545["fg"] = "#000000"
        GButton_545["justify"] = "center"
        GButton_545["text"] = "車站資訊"
        GButton_545.place(x=250, y=190, width=70, height=25)
        GButton_545["command"] = self.GButton_545_command

        GButton_105 = tk.Button(root)
        GButton_105["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_105["font"] = ft
        GButton_105["fg"] = "#000000"
        GButton_105["justify"] = "center"
        GButton_105["text"] = "查詢位置"
        GButton_105.place(x=320, y=190, width=70, height=25)
        GButton_105["command"] = self.GButton_105_command
        self.root=root
    def GButton_985_command(self):
        self.root.withdraw()
        newWindow = tk.Toplevel(self.root)
        searchbook.App(newWindow)

    def GButton_545_command(self):
        station_data.create_treeview(self.root)

    def GButton_105_command(self):
        self.root.withdraw()
        newWindow = tk.Toplevel(self.root)
        avtrain.App(newWindow)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
