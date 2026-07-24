class Pet:  # This is the general class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what to say")


class Cat(Pet):  # This is the more specific class  --> Child class
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):  # This is the more specific class --> Child class
    def speak(self):
        print("Bark")


class fish(Pet):
    pass


p = Pet("Tim", 19)
p.speak()
c = Cat("billota", 20,"red")
c.show()
d = Dog("kutta", 23)
d.speak()
f = fish("bubbles", 2)
f.speak()
