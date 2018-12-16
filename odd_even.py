"""
    Ask the user for a number. Depending on whether the number is even 
    or odd, print out an appropriate message to the user. 
    Hint: how does an even / odd number react differently when divided by 2?
    Extras:
    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) 
    and one number to divide by (check). If check divides evenly into num, 
    tell that to the user. If not, print a different appropriate message.
"""


num = int(input("Tell me a number: "))
check = int(input("Give me the number to divide by: "))

if number % 2 == 0 & number % 4 != 0:
    print(num + "is even")
elif number % 2 == 1:
    print(num + "is odd")
else:
    print(num + "is multiple of 4")
    
if num % check == 0:
    print(check + "divides evenly into " + num)
else:
    print(check + "does not divide evenly into " + num)
    