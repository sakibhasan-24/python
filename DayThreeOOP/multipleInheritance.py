

class Vehicle:
    def move(self):
        print (f"{self.__class__.__name__} is moving")
        

class ElectricDevice:
    def charge(self):
        print (f"{self.__class__.__name__} is charging")

# Multiple Inheritance: inheriting from both classes

class SmartCar(Vehicle, ElectricDevice):
    def autoPilot(self):
        print (f"{self.__class__.__name__} is autopiloting")




# create instance of SmartCar
car = SmartCar()

# call methods from both classes
car.move()
car.charge()
car.autoPilot()

# Problem with this multiple inheritance

# The Diamond Problem
# we solve it using MRO
