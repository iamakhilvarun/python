import copy

animals = {
    "lion": ("scary", "big", "cat"),
    "elephant": ("big", "greay", "wrinkeled"),
    "teddy": ("cuddly", "stuffed"),
}
# Perform a shallow copy
# things= animals.copy()
# animals("teddy")="toy"

# Perform deep copy
things=copy.deepcopy(animals)
print(id(things("teddy")), things("teddy"))
print(id(animals("teddy")), animals("teddy"))
print()

things("teddy").append("toy")
print(things("teddy"))
print(animals("teddy"))
