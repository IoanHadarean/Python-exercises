"""
    Max digit sum and min digit sum for n numbers

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
    else:
        if(sum < min):
            min = sum
            b = m
    m = int(input())    
print(a)
print(b)


#am incercat sa le pun in niste variabile a = m, respectiv b =m(ca sa printez 
#m), dar n-a mers, nici macar nu da bine :(, viata cruda :(



    
    
    
    
    
    