# OOP Basics / Classes / Objects / Exceptions
# Everything in python is an object / Python can also be used as a scripting language
# type(int(5)) # this is instance of class 'int'
# type(int) # this is class 'type'
class Car:
    runs = True

    def __init__(self, name):
        print("New Car!")
        self.name = name

    def __str__(self):
        return print(f"Here is my {name} its nice huh?")
        
    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

# Inheritence -----------------------------------------
class Vehicle:
# Saving Args to the instance
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if fuel == "gas":
            return False
        else:
            return True

class Truck(Vehicle):

    def __init__(self, make, model, fuel='gas', num_wheels=4):
        super().__init__(make, model, fuel)
        self.num_wheels = num_wheels  
# Open REPL and import class vehicle, 
# Create a new vehicle to test     
# With python you can inherit from multiple classes at once.

user_input = "a"
try:
    int(user_input)
    print(f"great number: {user_input}")
except(ValueError):
    print("Thats not a num!")

# Want to catch more specific exception first
def division(num):
    try:
        result = 3.14 / num
    except ArithmeticError: 
        print("General Math Error")
    except ZeroDivisionError:
        print("Divide by zero error!")

division(0) # gives math error -- use exception hierarchy switch them around.
# Do not swallow exceptions IE....
try:
    int("a")
except Exception:
    pass
# Create custom exceptions
class MyCustomException(Exception):
    pass
# useful way of signaling error conditions in code.
class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got a bad value {value}"
        super().__init__(message)


        