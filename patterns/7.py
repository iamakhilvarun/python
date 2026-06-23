n=5
for i in range(n):
    for j in range(i+1): #prints increasing amount od spaces
        print(' ',end=' ')
    for j in range(i,n-1): # n-1 is for decreaing a coulmn 
        print('*',end=' ')# prints decreasing amount of stars 
    for j in range(i,n):# prints decreasing amount of stars
        print('*',end=' ')
    print()