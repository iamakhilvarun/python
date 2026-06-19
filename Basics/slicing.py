#                  1
#        01234567890123
parrot = "Norwegian blue"

# it tells that start with 0 but not print 6 (up to but not including)
print(parrot(0:6))  # Norweg

print(parrot(3:5))  # we

print(parrot(0:9))
print(parrot(:9))  # the default start value is 0

print(parrot(10:14))
print(parrot(10:))  # the default last value is 13
print()
print(parrot(:6))
print(parrot(6:))

print(parrot(:6) + parrot(6:))
print()
# there is no start value and no end value
print(parrot(:))
print()
letters = "abcdefghijklmnopqrstuvwxyz"

print(letters(0) + letters(10) + letters(7:9) + letters(11))
