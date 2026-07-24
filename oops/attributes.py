class Person:
    number_of_people = 0  # this is class attribute not related to any instance
    Gravity = -9.8

    # This is the method defined
    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Akhil")
p2 = Person("Tej")
print(Person.number_of_people_())