# OOP

# class means blueprint for creating objects 
# object is an instance of a class 
# Class has two main itesm ,one is attribute and other is methods


# create a class

class Person:
    # adding properties in class ,we called it attribute
    def __init__(self,name,email,age):
        # __init__ is a constructor method that runs automatically when an object is created
# self is a reference to the current instance of the class 
# and is used to access variables that belongs to the class
        # print(self)
        self.name = name
        self.email = email
        self.age = age

    # method
    def greet(self):
        return f"Hello {self.name} , you are {self.age} years old"


# now create an object of class

person1 = Person("sakib","sakib@gmail.com",30)
print (person1.age)
print(person1.greet())



# class variable and instance variable
# class variable is a variable that is shared by all instances of a class ,
# instance variable is a variable that is unique to each instance of a class
