from priscription_data import patients

trail_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}
while trail_patients:
    patient=trail_patients.pop()
    print(patient,end=" : ")
    priscription=patients(patient)
    print(priscription)
