# -*- coding: utf-8 -*-

import os
import pause
from datetime import datetime

# Check what directory you are currently in and show it in console
os.getcwd()
print (os.getcwd())

# Change the current directory to ("<your path>") and show that it was done in console
os.chdir("C:/Users/Alina/AppData/Roaming/Zoom/bin")
os.getcwd()
print (os.getcwd())


# After you run the program, wait until a specified date and time to execute following function
# syntax >> datetime(year,month,day,24hr,min)

time= datetime(2021,7,14,12,58)
pause.until(time)

# Force close any program

os.system("TASKKILL /F /IM Zoom.exe")
print ("\nThe program was closed at:",time)

