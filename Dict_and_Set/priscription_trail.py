from priscription_data import *

trail_patients = {"Denise", "Eddie", "Frank", "Georgia","Kenny"}
# Remove warfrin and add endoxban
for patient in trail_patients:
    priscription=patients(patient)
    if warfarin in priscription:
        priscription.remove(warfarin)
        priscription.add(edoxaban)
    else:
        print()
        print(f"Patient {patient} is not taking warfrain."
              f"Please remove {patient} form the trail")
    print(patient,priscription)

