animals = {
    "Turtle",
    "Horse",
    "Python",
    "Robin",
    "Swallow",
    "Hedgehog",
    "Wren",
    "Aardvark",
    "Cat",
}

birds = {"Robin", "Wren", "Swallow"}

print(f"birds is a subset of animals: {birds.issubset(animals)}")
print(f"animals is a superset of birds: {animals.issubset(birds)}")

print(f"birds is a superset of animals: {birds.issuperset(animals)}")
print(birds<=animals)
print(birds<animals)

print('*'*80)

garden_birds={"Robin", "Wren", "Swallow"}
print(garden_birds==birds)

print(garden_birds<=birds)
print(garden_birds<birds)

print('*'*80)

more_birds={"Wren", "Swallow","Budgie"}
print(garden_birds>=more_birds)