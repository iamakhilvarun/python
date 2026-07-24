class Pet:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    
class Dog(Pet):
    def __init__(self,name,sound):
        super().__init__(name,sound)

    def Name_of_dog(self):
        return self.name

    def Speak(self):
        return self.sound


d1=Dog("Bruno","woof!")
print(d1.Name_of_dog())
print(d1.Speak())