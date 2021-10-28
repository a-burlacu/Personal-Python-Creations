import subprocess
import pause
from datetime import datetime
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open File Explorer")
root.geometry("600x300+750+400")

def Buttonclick():
    path = Label(root,text=FileExplorer())
    path.pack()     

def FileExplorer():
    window = Toplevel(root)
    window.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path      



button = Button(root, text="Open File Explorer", command=lambda: Buttonclick())
button.pack(pady=20) 

 

root.mainloop()