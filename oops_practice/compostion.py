class Battery:
    def charge(self):
        print("battery charging......")


class Phone:
    def __init__(self):
        self.battery = Battery()  # Phone HAS-A Battery

    def power_on(self):
        self.battery.charge()
        print("Power is on")


bmw = Phone()
bmw.power_on()
