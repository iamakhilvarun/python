n = 5
for i in range(n):  # range(start,stop)
    for j in range(i, n):  # i added start and stop
        # now 1st it runs 0 to 5 then 1 to 5->4 then 2 to 5->3 then 3 to 5=>4 then 4 to 5=>1
        print("*", end=" ")
    print()# print at newline
