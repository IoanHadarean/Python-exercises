"""
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year 
    that they will turn 100 years old.
"""


name = input("What is your name: ")
print(name)
age = int(input("How old are you: "))
print(age)
year = str((2018 - age) + 100)
height = input("How tall are you?")
x = 4
for x in height:
    print(height)

print(name + " will be 100 years old in the year " + year)

