n = 5
for i in range(n):
    for j in range(i + 1):  # prints increasing spaces of each row
        print(" ", end=" ")

    for j in range(i, n - 1):  # n-1 is for decreaing a column
        print("*", end=" ")  # prints decreasing amount of stars(left half)

    for j in range(i, n):  # prints decreasing amount of stars(right half)
        print("*", end=" ")
    print()
