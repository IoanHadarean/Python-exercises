"""
    Ask the user for a number and print out whether the number
    is a palindrome or not.
"""

number = int(input("Please enter a number: "))

num = number #we need to declare another variable that stores the input


v = 0

#Watch out, in Python / returns a float

while(num > 0):
    i = num % 10   #takes every digit of the number
    v = v * 10 + i  #appends each digit in a new number
    num = num//10    #goes through the number digits until it reaches 0

#Be careful you compare the stored number
#from the input with the new number  
    
if(number == v):
    print("%d is palindrome" % number)
else:
    print("%d is not palindrome" % number)
    

#test   
#num = 121     12    1        0
#i =   0       1     2        1
#v =   0       1     12      121 