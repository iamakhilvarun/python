shopping_list= ["milk","pasta","eggs","spam","bread","rice"]
# for item in shopping_list:
#     if item !="spam":
#         print("Buy "+ item)

for item in shopping_list:
    if item == "spam":
        continue#🔁 What is continue in Python?
                 # skip the current iteration and move to the next one
    print("Buy "+item)

print("-----------------")
for item in shopping_list:
    if item == "spam":
        break #immediately stop the loop, even if items are still left.
    print("Buy "+item)

 