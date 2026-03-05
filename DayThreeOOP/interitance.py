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



class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Cow(Animal):
    pass


# create instance of child class

dog=Dog("dog")
cat=Cat("cat")
cow=Cow("cow")

# call methods
dog.eat()
dog.sleep()
print(dog.name)