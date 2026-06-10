# farm_animals ={"horse","goat","hen","cow","sheep"}
# wild_animals={"lion","elephant","tiger","panther","goat","horse"}

# all_animals_1=farm_animals.union(wild_animals)
# print(all_animals_1)

# all_animals_2=farm_animals.union(wild_animals)
# print(all_animals_2)

# all_animals_3=wild_animals | farm_animals # union 
# print(all_animals_3)

from priscription_data import adverse_interactions
meds_to_watch=set()
# for interations in adverse_interactions:
#     # meds_to_watch=meds_to_watch.union(interations) # creates a new set , original stays unchanged
#     # meds_to_watch=meds_to_watch | interations # same, creates new set
#     # meds_to_watch.update(interations) # modify the existing set , no new set created
#     meds_to_watch |= interations # shorthand for update() same same

meds_to_watch.update(*adverse_interactions)
# The * operator is unpacking it tkaes the items form the list and passes then as seperate arguments
print(sorted(meds_to_watch))
print(*sorted(meds_to_watch),sep='\n')