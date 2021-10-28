import os
import pause
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Create main window
root = Tk()

# Main window title and size + position on screen
root.title("Auto Exit Program")
root.geometry('400x300+750+400')

# Display input messages
message = Label(root, text="Set Hour (24HR):")
message.place(x=10,y=10)
message1 = Label(root, text="Set Minute:")
message1.place(x=120,y=10)


# Define options for dropdown menus to select time
hour = IntVar()
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
myHour = ttk.Combobox(root, values=hours, state="readonly", width=4)
myHour.current(0)
myHour.place(x=30,y=30)



minute = IntVar()
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
myMinute = ttk.Combobox(root, values=minutes, state="readonly", width=4)
myMinute.current(0)
myMinute.place(x=130,y=30)



# Function that shows selected date and time for operation to occur 
def SelectTime():
    today = datetime.today()
    todayLabel = Label(root, text="Date: "+ today.strftime("%m/%d/%y"))
    todayLabel.place(x=10,y=180)

    myHourLabel = Label(root, text="Hr: "+ myHour.get())
    myHourLabel.place(x=100,y=180)

    myMinLabel = Label(root, text="Min: "+ myMinute.get())
    myMinLabel.place(x=150,y=180)



# Function that opens File Explorer and returns selected location path
def FileExplorer():
    window = Toplevel(root)
    window.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path 



# Function that displays results of FileExporer function (i.e. path name)
def Buttonclick():
    path = Label(root,text="File Path:\n"+ FileExplorer())
    path.place(x=5,y=80)



# Button to open File Explorer
button = Button(root, text="Open File Explorer", command=lambda: Buttonclick())
button.place(x=250,y=20)



# Button that executes main command (displays execution date/time)
runButton = Button(root, text="Run Program", command=SelectTime)
runButton.place(x=160,y=250)


# Keep displaying the window
root.mainloop()

