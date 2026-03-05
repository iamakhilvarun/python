#                  1
#        01234567890123
parrot = "Norwegian blue"
# the slice starts at index 0
# it extends up to (nut not including) position 6
# we step through the sequence in step of 3
print(parrot[0:6:2])  # Nre

print(parrot[0:6:3])  # Nw

Number = "9,232;564:236 745;234"
seperators = Number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in Number).split()
print([int(val) for val in values])
