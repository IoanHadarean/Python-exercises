"""
    Ask the user for a string and print out whether 
    this string is a palindrome or not. (A palindrome 
    is a string that reads the same forwards and backwards.)
"""

string = str(input("Tell me a string: "))

reverse = string[::-1].upper()
string = string.upper()

if(reverse == string):
    print("The string is palindrome")
else:
    print("The string is not palindrome")
 
 
        
