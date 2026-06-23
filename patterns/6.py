n=5
for i in range(n):
    for j in range(i,n): # prints decreasing number of stars 
        print(" ",end=' ')
    for j in range(i):# this loop prints one less column
        print('*',end=' ')
    for j in range(i+1): # prints increasing number of stars in each row
        print('*',end=' ')
    print()
    