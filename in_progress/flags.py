cul = "rnagvpm"
def show(sol, k, cul, nrsol):
    print("solution number {0} ".format(nrsol))
    for i in range(0, k+1):
        print("{0} ".format(cul(sol[i])))

def validate(sol, k):
    v = 1
    for i in range(0, k):
        if(sol[i] == sol[k]):
            v = 0
    if (k == 1 & (sol[k] == 2 | sol[k] == 5)):
            v = 0
    return v

        
def backtrackingi(cul):
    sol= []
    k = 0
    nrsol = 0
    sol[k] = -1
    while(k >= 0):
        if(sol[k] < 6):
            sol[k] += 1
            if(validate(sol, k) == 1):
                if(k == 2):
                    nrsol += 1
                    show(sol, k, cul, nrsol)
                else:
                    k+= 1
                    sol[k] = -1
        else:
            k -= 1

backtrackingi("rnagvpm")
# def main():
#     cul = "rnagvpm"
#     backtrackingi(cul)
        
# if __name__ == "__main__":
#     main()


 
# from operator import itemgetter 
 
# inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
# getcount = itemgetter(0)
# map(getcount, inventory)
# [3, 2, 5, 1]
# sorted(inventory, key = getcount)
# [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

# print((getcount, inventory))


 
