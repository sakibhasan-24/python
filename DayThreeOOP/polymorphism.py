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


