# OOP

# class means blueprint for creating objects 
# object is an instance of a class 
# Class has two main itesm ,one is attribute and other is methods


# create a class

class Person:
    # adding properties in class ,we called it attribute
    def __init__(self,name,email,age):
        # print(self)
        self.name = name
        self.email = email
        self.age = age


# now create an object of class

person1 = Person("sakib","sakib@gmail.com",30)
print (person1.age)