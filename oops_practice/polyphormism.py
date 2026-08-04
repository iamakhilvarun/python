class Animal:  # Base class (Parent class)
    def speak(self):  # Method
        pass


class Dog(Animal):  # Child class (Subclass)
    def speak(self):  # Overridden method
        print("Woof!")


class Cat(Animal):  # Child class (Subclass)
    def speak(self):  # Overridden method
        print("Meow!")


class Cow(Animal):  # Child class (Subclass)
    def speak(self):  # Overridden method
        print("Moo!")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()
