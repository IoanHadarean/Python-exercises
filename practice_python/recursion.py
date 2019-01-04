def afis(i):
    if i >= 0:
        print(a[i], end = " ")
        afis(i-1)
        print("q")

if __name__ ==  "__main__":
    n = int(input())
    a = []
    line = input()
    split_line = line.split(" ")
    for i in range (n):
        a.append(int(split_line[i]))
    afis(n-1)
    print("y")