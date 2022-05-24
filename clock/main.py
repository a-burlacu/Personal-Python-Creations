from tkinter.ttk import *
from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")
root.geometry('+2650+200')
root.overrideredirect(True)


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


def button(event):
    window = Toplevel(root)
    window.geometry('+3150+230')
    window.overrideredirect(True)

    exit_button = Button(window,
                         text="EXIT",
                         bd=40,
                         bg="white",
                         fg="red",
                         activebackground="red",
                         activeforeground="white",
                         relief="raised",
                         command=close_program,
                         font=("Digital-7 Mono", 50))

    exit_button.pack(anchor='center')


def close_program():
    root.after(200, root.destroy)


root.bind('<Button>', button)

label = Label(root,
              font=("Digital-7 Mono", 180),
              background="black",
              foreground="firebrick")

label.pack(anchor='center')

time()

mainloop()
