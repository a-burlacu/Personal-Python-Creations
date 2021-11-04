"""
Task: Take a user input temperature in Fahrenheit, t, and convert to Celsius. 
Display initial temp plus 10 following temps.

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


