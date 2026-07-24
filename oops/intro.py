# def hello():
#     print("hello")


# x=1
# print(type(hello))

# string="hello"
# print(string.upper())


class Dog:
    def __init__(self, name,age):
        self.name = name   # self.name is a attribute for class Dog
        self.age=age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age=age
        
d = Dog("nigga",9)
d.set_age(23)
print(d.get_age())