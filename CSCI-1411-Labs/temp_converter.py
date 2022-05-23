"""
Task: Take a user input temperature in Fahrenheit and convert it to Celsius.
"""
def temp_converter():

    temp = int(input("What is the Fahrenheit temperature? "))

    celsius = int((temp-32)*5/9)

    print("The Celsius temperature is:",celsius,"degrees.\n")

temp_converter()