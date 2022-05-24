"""
Resources used: 
ASCII Chart
https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
Python Code Visualizer
http://pythontutor.com/visualize.html#mode=edit
"""


# create new function to encrypt using caesar cipher
def encrypt(text, s):
    # create empty string to add new characters to
    # look at every letter in the input string and determine if upper or lower

    # if upper: find ASCII num for letter, add the shift (s) and subtract the
    # ASCII num for capital A (beginning of alphabet) then use modulo 26 to find
    # the location of the letter in the alphabet, and add 65 to it to get correct
    # place for new character, using chr() to change the ASCII num to a symbol

    # if lower: exact same process, but use 97 instead of 65  since 97 = 'a'
    # if character is a space, number, or symbol like !@#$% just pass it through
    # using the else:

    encrypted = ""
    for c in text:
        if (c.isupper()):
            encrypted += chr((ord(c) + s - 65) % 26 + 65)
        elif (c.islower()):
            encrypted += chr((ord(c) + s - 97) % 26 + 97)
        else:
            encrypted += c

    return encrypted


# create new function to decrypt message using caesar cipher  
# follow similar process but reverse adding the shift (s) and 65 (or 97)
def decrypt(encrypted_text, s):
    decrypted = ""
    for c in encrypted_text:
        if (c.isupper()):
            decrypted += chr((ord(c) - 65 - s) % 26 + 65)
        elif (c.islower()):
            decrypted += chr((ord(c) - 97 - s) % 26 + 97)
        else:
            decrypted += c

    return decrypted


# define main function which asks for user's input and also combines both 
# the encrypt and decrypt functions    
def main():
    text = input("\nEnter plaintext to encrypt: ")
    s = int(input("Enter shift: "))
    print("\nEncrypted text: " + encrypt(text, s))

    encrypted_text = input("\n\nEnter encrypted text: ")
    s = int(input("Enter shift: "))
    print("\nDecrypted text: " + decrypt(encrypted_text, s))


main()
