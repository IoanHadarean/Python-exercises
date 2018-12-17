n = int(input())
    
sum = 0

for i in range(1, n+1):
    a = 1
    for j in range(1, i+1):
    	a = a * i
    sum = sum + a
print("Rezultatul este {0}".format(sum))