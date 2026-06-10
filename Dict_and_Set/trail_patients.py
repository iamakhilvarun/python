# trail_1={"Bob","John","Charley","Georgia"}
# trail_2={"Anne","Charley","Eddie","Georgia"}

# check_set=trail_1.intersection(trail_2)
# print(check_set)

farm_animals = {"horse", "goat", "hen", "cow", "sheep"}
wild_animals = {"lion", "elephant", "tiger", "panther", "goat", "horse"}
potential_rides = {"donkey", "horse", "camel"}

interesection = farm_animals & wild_animals & potential_rides
print(interesection)

mounts=farm_animals.intersection(wild_animals,potential_rides)
print(mounts)