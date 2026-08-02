class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work,but i am flying")
        else:
            print("I think i will just walk ;( ")


class Duck(object):
    def __init__(self):
        self._wing=Wing(1.8)

    def walk(self):
        print("Waddle,waddle,waddle")

    def swim(self):
        print("Come on it, the water is lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()

class penguin:
    def walk(self):
        print("Waddle,waddle,waddle")

    def swim(self):
        print("Come on in, it's a bit chilly this far South")

    def quack(self):
        print("come swim with me twin ,FR twin!!")


# def test_duck(duck):
# duck.walk()
# duck.swim()
# duck.quack()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
    # percy = penguin()
    # test_duck(percy)
