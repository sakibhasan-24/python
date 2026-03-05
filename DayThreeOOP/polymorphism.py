# build in polymorphism

print(len("hello"))
print(len([1,2,3,4]))
print(len({"a":1,"b":2}))

#operator polymorphism
print(5 + 3)
print("Hello " + "World")
print([1,2] + [3,4])



# basic polymorphism
""" All objects have the same method name speak(),
but each behaves differently """
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

def animal_sound(animal):
    print(animal.speak())


cat=Cat()
dog= Dog()

animal_sound(cat)
animal_sound(dog)


# polymorphism with inheritance


""" This is method overriding, a form of polymorphism. """
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# duck typing
""" This is also a form of polymorphism. """
# Object works if it has required method.

class Bird:
    def fly(self):
        print("Flying")

class Airplane:
    def fly(self):
        print("Airplane flying")
    def move(self):
        print("Moving")

def start_flying(obj):
    print(obj)
    obj.fly()
    obj.move()

start_flying(Bird())
start_flying(Airplane())