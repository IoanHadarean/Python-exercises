
n = int(input("Enter a number: "))



sum = 0
i = 1
list = []

while(i < n//2):
    sum = 0
    for i in range(1, n//2):
        sum = sum + i
    if(sum == n):
        list.append(i)
        print(list)
    if i >n:
        break
    
            
"""
v =     1  2
sum =   0  1
i=      1  2
"""