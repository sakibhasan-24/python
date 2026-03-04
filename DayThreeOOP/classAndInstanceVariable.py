# let's create a flyover car passing system using class and instance variable

from datetime import datetime
class CrossingSystem:
    # class variable
    total_cars = 0

    def __init__(self, name):
        # instance variable
        self.name = name
        self.cars = []
        # increment the total_cars by 1
        CrossingSystem.total_cars += 1

    def add_car(self, car):
        self.cars.append(car)


# create two crossing system
crossing1 = CrossingSystem("mustaz crossing, dhaka, bangladesh,car no:QWERTY")
crossing2 = CrossingSystem("mustaz crossing, dhaka, bangladesh,car no:ASDFGH")
crossing3 = CrossingSystem("mustaz crossing, dhaka, bangladesh,car no:ZXCVBN")

# CrossingSystem.total_cars=0

print(f"{crossing1.total_cars} total car crossing till {datetime.now()}")