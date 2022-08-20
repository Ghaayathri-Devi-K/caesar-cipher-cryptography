'''
The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

~ asks the user for one line of text to encrypt;
~ asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
~ prints out the encoded text.

Test your code using the data we've provided.

------ Test data 1 -------
Sample input:
abcxyzABCxyz 123
2

Sample output:
cdezabCDEzab 

------ Test data 2 -------
Sample input:
The die is cast
25

Sample output:
Sgd chd hr bzrs
'''

def caesar_cipher_encrypt_mod(string, shift):
    if shift in range(1,26):
        cipher = ''
        for i in string:
            if not i.isalpha():
                continue
            else:
                code_point = ord(i)
                if code_point in range(ord('a'),ord('z')+1):
                    new_code = code_point + shift
                    if new_code > ord('z'):
                        new_code = new_code - 26
                elif code_point in range(ord('A'),ord('Z')+1):
                    new_code = code_point + shift
                    if new_code > ord('Z'):
                        new_code = new_code - 26
            cipher = cipher + chr(new_code)        
        return cipher

    else:
        print('''Oops! The text cannot be encrypted...
            Your shift should be between 1 and 25...''')

# Test case 1
string = 'abcxyzABCxyz 123'
shift = 2
caesar_cipher_encrypt_mod(string, shift)

# Test case 2
string = 'The die is cast'
shift = 25
caesar_cipher_encrypt_mod(string, shift)
