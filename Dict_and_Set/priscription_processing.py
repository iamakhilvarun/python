from priscription_data import patients

trail_patietns = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}
while trail_patietns:
    patient=trail_patietns.pop()
    print(patient,end=" : ")
    priscription=patients[patient]
    print(priscription)
