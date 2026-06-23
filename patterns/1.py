n=5
# print("*"*n)
# first row is for rows how many rows it will print for 
for row in range(n):# this loop will print next loop n times
    # The second loop is for column how many colums are there for 
    for column in range(n):
        print('*',end=' ') # end='' overwrites the newline and we can get stars in one line 
    print() # This is added cuz whenever the first loops end it prints newline so we can get stars on newline 