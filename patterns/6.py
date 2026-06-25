n=5
for i in range(n):
    for j in range(i,n): # prints decreasing number of spaces
        print(" ",end=' ')
    for j in range(i):# this loop prints one less column (left half)
        print('*',end=' ')
    for j in range(i+1): # prints increasing number of stars in each row (rigth half)
        print('*',end=' ')
    print()
    