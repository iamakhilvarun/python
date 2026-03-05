letters = "abcdefghijklopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)  # we get the string reversed
# there is no need to start and end cuz step slicer will is (-) so it will count backwords automatically

# slice the string to produce 8 characters in reverse order
challenge3 = letters[25:-9:-1]
print(challenge3)  # zyxwvuts

# slice the string to produce edcba
challege2 = letters[4::-1]
print(challege2)  # edcba

# create a slice that produces the charecters qpo
challenge1 = letters[-10:-13:-1]
print(challenge1)  # qpo


print()
print(letters[-4:])  # wxyz
print(letters[-1:])  # z
print(letters[:1])  # a
print(letters[0])
