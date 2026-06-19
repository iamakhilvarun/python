morning = ("Java","Ruby", "C#", "C", "Lisp")
afternoon = ("Python", "C#", "Java", "C", "Ruby")

possible_courses =set(morning).symmetric_difference(afternoon) # (^) can be used
print(possible_courses)

possible_courses=set(afternoon).symmetric_difference(morning)
print(possible_courses)