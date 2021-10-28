import os
import pause
from datetime import datetime

# Check what directory you are currently in and show it in console
os.getcwd()
print (os.getcwd())

# Change the current directory to ("<path>") and show that it was done in console
os.chdir("C:/Users/Alina/AppData/Roaming/Zoom/bin")
os.getcwd()
print (os.getcwd())

# After you run the program, wait until a specified date and time to execute following function

# syntax >> datetime(year,month,day,24hr,min)
time= datetime(2021,10,21,00,52)
pause.until(time)

# Force close any program    Zoom.exe
os.system("TASKKILL /F /IM Zoom.exe")


print ("\nThe program was closed at:",time)

























"""
shit that didn't work:

"""
#‪C:\Users\Alina\AppData\Roaming\Zoom\bin\Zoom.exe
# def open_program (path_name):
   
#     return subprocess.Popen(path_name)

#    #return subprocess.Popen(["cmd", "/c", "dir", "Roaming/Zoom/bin/Zoom.exe"])

# def close_program(p):
#     p.terminate()
# path = '/Alina/AppData/Roaming/Zoom/bin/Zoom.exe'    
    
# path_name = ["cmd", "/c", "dir", "AppData/Roaming/Zoom/bin/Zoom.exe"]
# open_program(path_name)
# p=open_program(path_name)
# time.sleep(3)
# close_program(p)