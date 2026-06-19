animals = {
    "lion": ("scary", "big", "cat"),
    "elephant": ("big", "greay", "wrinkeled"),
    "teddy": ("cuddly", "stuffed"),
}
things={}

def deep_copy(data):
    copied={}
    for key ,value in data.items():
        copied(key)=value.copy()
    return copied

things=deep_copy(animals)

things("teddy").append("toy")

print(things)
print(animals)