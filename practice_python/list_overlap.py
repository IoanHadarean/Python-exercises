"""
    Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains 
    only the elements that are common between the lists 
    (without duplicates). Make sure your program works on 
    two lists of different sizes.
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [99]

"""
    Long version

list = []

for i in a:
    if i in b & i not in list: 
        list.append(i)
        
print(list)
"""
        
print(list(set(a) & set(b)))


"""
print(sorted(set(a+b))) #gets all the elements from both arrays(without duplicates)
"""
    
    

    