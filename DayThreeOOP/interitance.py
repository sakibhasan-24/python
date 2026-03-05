# what is inheritance----> inheriting properties and methods
#  from a parent class to a child class





# create base class
class Animal:
    def __init__(self,name):
        self.name=name
        is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

