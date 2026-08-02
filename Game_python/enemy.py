import random

class Enemy:
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"I took {damage} points damage and have {self._hit_points} left")
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self._name} lost a life")
            else:
                print(f"{self._name} is dead")
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(
            self
        )


class Troll(Enemy):
    def __init__(self, name):
        # super(Troll,self).__init__(name=name,lives=1,hit_points=23) --> this is used in python 2
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f"Me {self._name}. {self._name} stomp you")


class Vampire(Enemy):# subclass of Enemy(superclass)
    def __init__(self, name):
        super().__init__(name=name, lives=4, hit_points=60)


    def dodges(self):
        if random.randint(1,3)==3:
            print(f"****** {self._name} doges ******")
            return True
        else:
            return False

    def take_damage(self,damage):
        if not self.dodges():
            super().take_damage(damage=damage)

    
class Vampire_king(Vampire):
    def __init__(self,name):
        super().__init__(name)

        self._lives=1
        self._hit_points=140    

    def take_damage(self,damage):
        damage //= 4 # reduce damage by quarter half
        super().take_damage(damage)