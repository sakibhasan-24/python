# we can't instantiate abstract class

""" An abstract class defines a blueprint that child classes must implement. """
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass 

class Bkash(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} via Bkash.")

class Card(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} via Credit Card.")

# p = Payment()  
my_payment = Bkash()
my_payment.process_payment(500)


""" 
        Create abstract class
        ↓
Mark abstract methods
        ↓
Store them in __abstractmethods__
        ↓
Prevent object creation if not implemented
        ↓
Subclass must implement them
        ↓
Then subclass becomes concrete

A class that defines a blueprint and forces subclasses to implement certain methods.
 """