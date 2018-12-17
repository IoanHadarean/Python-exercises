n = int(input())

sum = 0

for i in range(1, n+1):
    p = 1
    for j in range(1, i+1):
        p = p * j
    sum = sum + p 
print("Rezultatul este {0}".format(sum))