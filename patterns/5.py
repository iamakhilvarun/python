n=5 
for i in range(5):
    for j in range(i+1):
        print(" ",end=' ')# print increasing spaces each row
    for j in range(i,n):
        print('*',end=' ')# print decreasing stars each row
    print()