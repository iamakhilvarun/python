vehicles = {
    "dream": "Honda 250 T",
    "roadster": "BMW R110",
    "er5": "Kawaski ER5",
    "can-am": "Bombardier can-am 250",
    "virago": "Yamaha XV250",
    "tenere": "Yamaha XT650",
    "jimny": "Suzuki jimny 1.5",
    "fiesta": "Ford Fiesta Ghia 1.4",
    "roadster":"Triumph street triple"
}
# my_car=vehicles['fiesta']
# print(my_car)

# commuter=vehicles['virago']
# print(commuter)

# learner=vehicles.get("er5")
# print(learner)


vehicles["starfighter"]="Lockheed F-104"
vehicles["learjet"]= "Bombardier learjet 75"
vehicles["toy"]= "Glider"

#upgrade the virago
vehicles["virago"] ="Yamaha XV535"
del vehicles["starfighter"]
# del vehicles["f1"]

# If you dont want the program to crash add None as default value 
result=vehicles.pop("f1","Nigga your broke ass cant buy a f1 try selling yourself to a demon may that works?")
print(result)
plane=vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere","not present")
print(bike)
print()
# for key in vehicles:
#     print(key,vehicles[key],sep=" ,")
for key ,value in vehicles.items():
    print(key,value,sep=", ")