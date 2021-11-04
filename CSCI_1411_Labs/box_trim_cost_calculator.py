"""
Trim only comes in 12" segments at $1.88 a piece. 
Task: 
Given dimensions of a box, report the perimeter length, number of segments needed,
total cost of all segments, amount of unused trim, and cost of unused trim.

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