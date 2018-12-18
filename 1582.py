
"""
n = int(input())

sum = 0
max = -1
min = 1000


m = int(input())
aux = m
for j in range(1, n):
    while(aux != 0): 
        digit = aux % 10
        sum = sum + digit
        aux = aux // 10
    if(sum > max):
        max = sum
        a = m
    m = int(input())    
print(m)
"""

n = int(input())

sum = 0
max = -1
min = 1000

m = int(input())
aux = m
for j in range(1, n):
    while(aux != 0): 
        digit = aux % 10
        sum = sum + digit
        aux = aux // 10
    if(sum < min):
        min = sum
        a = m
    m = int(input())
print(m) 

#n-am stiut sa le pun pe ambele in aceeasi solutie, desi dau bine, separat



    
    
    
    
    
    