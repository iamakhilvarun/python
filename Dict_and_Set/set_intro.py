farm_animals={'cow','sheep','cow','horse','hen','goat'}
print(farm_animals)
# Set are unorderd
for animal in farm_animals:
    print(animal)

print()

print("Indexing a sequence")
animals_list=('cow','sheep','cow','horse','hen','goat')
goat=animals_list(5)
print(goat)

# print("Indexing a set is not possible")
# goat=farm_animals(5)
# print(goat)
more_animals={'sheep','cow','goat','horse','hen'}
if more_animals==farm_animals:
    print('The sets are equal')
else:
    print('The set are diffrent')