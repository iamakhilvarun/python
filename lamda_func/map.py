# map() is a built-in Higher-Order Function that applies a function to every element of an iterable.
# map(function, iterable)
l = [1, 2, 3, 4, 5, 6]

a = list(map(lambda x: x * 2, l))

print(a)


b = list(map(lambda x: x % 2 == 0, l))
print(b)


students = [
    {
        "name": "Aarav Sharma",
        "address": "24 Lake Road, Pune",
        "father_name": "Rajesh Sharma",
    },
    {
        "name": "Riya Patel",
        "address": "18 Green Park, Ahmedabad",
        "father_name": "Sanjay Patel",
    },
    {
        "name": "Arjun Nair",
        "address": "42 Palm Grove, Kochi",
        "father_name": "Suresh Nair",
    },
]

c = list(map(lambda student: student["name"], students))
print(c)
