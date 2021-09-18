# Open and read the file with test numbers
# Create a writeable output file
infile = open("testCCNums.txt","r")
outfile = open("CCoutput.txt","w")  

# Define new variable,use readlines to read every line into a list

lines = infile.readlines()

# For every line, stripped of extra characters, store this as the card number

for line in lines: 
    card_num = line.strip()

# Store the length of the card number as a variable, then check if = 15 or 16

    card_len = len(card_num)
    if card_len==15 or card_len==16: 
    
# Create new empty lists to use in for loops   
     
        card_list=[]
        card_others=[]
        sum_digits=0
        
# This takes every item in the card_num, starting at the -2 (second to last) 
# and continuing through the entire string backwards using steps of -2
# Then append the empty list to include integer values of the items selected
# Finally, perform arithmetic using list comprehension, taking every item
# on the list and multiplying it by 2     

        for num in card_num[-2::-2]:
            card_list.append(int(num))
            doubles=[i*2 for i in card_list]
            
# This takes every integer that's been doubled and checks if it is a double 
# digit integer (>9), if it is, take the modulo 10 of the number and add 1
# Ex. 16 = 16%10 = 6     then 6 + 1 = 7   to find the sum of the digits
# if it's single digit integer, simply add it to the total sum of the digits 
         
        for digit in doubles:
            if digit >9:
                digit=(digit%10)+1
                sum_digits+=int(digit)
            else:
                sum_digits+=int(digit)
                
# This takes every other item in the original string, card_num, starting at 
# the last digit and going backwards in steps of -2 then adding to the list  
# We do this so we can add ALL the digits in the card number together 

        for num in card_num[-1::-2]:
            card_others.append(int(num))
            
# This takes each integer from the previous list and adds it to the sum total
    
        for digit in card_others:
            sum_digits+=int(digit)
            
# This checks if the sum total is completely divisible by 10 (a 0 remainder)
    
        if sum_digits%10==0:
            
# If the sum is divisible by 10, we can go on to the next step to see which  
# type of card it is. If it's not, then the card is invalid and the program
# will skip down to the "else:" statement 
# Name a blank variable cardtype, so the value can change using the if/elif   
    
            cardtype = "" 

# Check the card number's index 0 position, if it =4 this is a Visa, so set 
# the cardtype to Visa, and print the following statement to the output file
# The sybtax for printing to an output file is print( x + y + z, file= output)
            
            if card_num[0]=='4':
                cardtype = "VISA"
                print(card_num+"--------"+cardtype+":VALID", file = outfile)
                
# Second choice if the first digit was not 4: check the index from 0:2 of the
# card number, if it equals 51,52,53,54,55 then cardtype = Mastercard
# Print the statement to the output file   
              
            elif card_num[0:2]=='51'or card_num[0:2]=='52' or card_num[0:2]=='53'\
                or card_num[0:2]=='54' or card_num[0:2]=='55':
                cardtype = "MASTERCARD"
                print(card_num+"--------"+cardtype+":VALID", file = outfile)

# Similar to MAstercard, check the first two digits ([0:2]) to see if they 
# = 34 or 37 and declare cardtype as American Express, print to output file 
               
            elif card_num[0:2]=='34'or card_num[0:2]=='37':
                cardtype = "AMERICAN EXPRESS"
                print(card_num+"--------"+cardtype+":VALID", file = outfile) 
 
# If the number fails the initial 'if' statement, where the sum is divisible
# completely by 10, print the card number with the invalid statement in the
# output file  
              
        else: 
            cardtype = ''
            print(card_num+"--------"+cardtype+":INVALID", file = outfile)    

# Make sure to close both the input file and the output file                
                
infile.close()
outfile.close()

# Print a statement declaring the program has been completed, so the user
# knows the program worked 

print("Results have been written to: 'CCoutput.txt'")
