"""
Given a list of numbers and a number k, return whether 
any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return
true since 10 + 7 is 17.
"""


n = int(input())
k = float(input())
line = input()
split_line = line.split(" ")
list = []
count = 0


for i in range(n):
    list.append(int(split_line[i]))
print(list)

for number in list:
    if k - number in list and list.count(number) > 1:
        count += 1
print(count)