class Teacher:
    def __init__(self,name):
        self.name=name

    def teach(self):
        print("Rahul is teaching")

class School:
    def __init__(self,teacher):
        self.teacher=teacher
    
    def conduct_class(self):
        self.teacher.teach()

teacher=Teacher("Rahul")
school=School(teacher)
school.conduct_class()