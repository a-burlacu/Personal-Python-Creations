"""
Problem Statement:  
You will convert all the temperatures from the initial value entered to the initial value entered plus 10 degrees. (For example, if the user enters 32 degrees, you will print out the conversion to celsius for 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, and 42 degrees.)
Task:
Create a program that does the following things:
    1. Ask the user for the initial temperature in Fahrenheit.
    2. Calculates the conversion of temperature to Celsius. 
    3. Converts the range of temperatures from the initial to the inital + 10 degrees.
    4. Prints the conversion for each of the temperatures. 
"""
def temp_converter():

    t = int(input("What is the Fahrenheit temperature? "))
    print("Your temperature plus the next 10 temperatures in Celsius are:")

    # starting with t, iterate through till t+11
    for i in range(t, t+11):

    # round the converted temp to 2 decimal places
        cel = round(((t-32)*5/9),2)

        print("\t",t, "degrees Fahrenheit is",cel,"degrees Celsius.")

    # redefine t so the loop will move forward until it reaches t+11
        t += 1

temp_converter()