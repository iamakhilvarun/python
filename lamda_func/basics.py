# A lambda function is a small, anonymous function that is written in one line.
a = lambda x: x + 2

print(a(2))

b = lambda x: x[0] == "a"

print(b("apple"))
print(b("banana"))


b = lambda x: "Even" if x % 2 == 0 else "odd"

print(b(2))
print(b(3))
