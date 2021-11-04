"""
Problem Statement:
You have a box that has a length and width in inches. These lengths and widths are not restricted to be in whole numbers (e.g, the length could be 11.2 inches).
You want to put trim around the box, but the local HW store only sells trim in 12” segments. A 12” segment of trim costs $1.88. 
Task:
Create a program that does the following things:
    1. Ask the user the length, in inches, of the box.
    2. Ask the user the width, in inches, of the box.
    3. Calculates the perimeter of the box and prints that out (perimeter = 2*L + 2*W)
    4. Calculates and the number of segments needed to trim the box (around the perimeter)
    5. Prints the int version of number of segments
    6. Calculates the cost of the trim 
    7. Calculate the amount of $$ you lost because you could not buy the trim in 
        increments other than 12” segments 
"""
def trim_calculator():

    l = float(input("Enter length in inches: "))
    w = float(input("Enter width in inches: "))

    per = (2*l)+(2*w)
    per_int = int(per)   # always rounds down to whole number
    
    print("The perimeter of your box is:",f'{per:.2f}',"inches.")

    total_seg = int((per_int/12))+1
    total_trim = total_seg*12
    print("You will need to purchase",total_seg,"segments of trim.")

    total_cost = ((total_seg)*1.88)
    print("The total cost of trim is: $",f'{total_cost:.2f}')

    extra_trim = round((total_trim-per),2)
    print("You will have",f'{extra_trim:.2f}',"inches trim leftover.")
   
trim_calculator()