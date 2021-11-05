"""
Resources used: 
ASCII Chart
https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
Python Code Visualizer
http://pythontutor.com/visualize.html#mode=edit
"""

# create function to determine if upper/lower letters in key and assign
# them ASCII numbers in a list format

def encrypt(text,key):
    keycode = []

    for i in key:
        if(i.isupper()):
            keycode.append(ord(i)-65)
        if(i.islower()):
            keycode.append(ord(i)-97)
         
     
    print (keycode)

# User inputs for function

text = input("\nEnter plaintext to encrypt: ")
key = (input("Enter encryption key: "))
encrypt(text,key)
