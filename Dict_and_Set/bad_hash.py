data = [
    ("orange", "a sweet ,orange, citrus fruit"),
    ("apple", "good for makeing cider"),
    ("lemon", "a sour yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juciy"),
]

# print(ord("a"))
# print(ord("b"))
# print(ord("z"))


def simple_hash(s:str)-> int:
    """ A ridiculously simple hash function"""
    basic_hash=ord(s[0])
    return basic_hash % 10
# This hash function takes the first character of a string, converts it to a number using ord(),
#  then returns the remainder when divided by 10. 
# Different words starting with the same letter will get the same hash, causing collisions.

def get(k:str)->str:
    """Return the value for a key , or none if the key doesnt exist"""
    hash_code=simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None 
keys= [""]*10
values=keys.copy()

for key , value in data:
    h=simple_hash(key)
    # h=hash(key)
    print(key,h)
    keys[h]=key
    values[h]=value

print(keys)
print(values)
print()

value=get("banana")
print(value)