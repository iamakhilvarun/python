n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')# print decreasing spaces each row
    for j in range(i+1):
        print('*',end=' ')# print increasing stars each row
    print()