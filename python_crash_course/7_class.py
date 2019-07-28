# Basic class
class Dog():
    """ The dog class. """
    """
    A function that’s part of a class is a method. Every method call associated 
    with a class automatically passes self, which is a reference to the 
    instance itself.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("A new dog called {} is here!".format(self.name.title()))
        # Python automatically returns the created instance. 

    def sit(self):
        print(self.name.title() + " is now sitting!")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

d = Dog("dob", 5)
d.sit()
d.roll_over()

# a Default Value for an Attribute
class Car():
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


"""
Inheritance.
"""

"""
The first task Python has when creating an instance from a child class is to
assign values to all attributes in the parent class. To do this, the __init__()
method for a child class needs help from its parent class.
"""
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.    
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_descriptive_name(self):
        """Overiden version. Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model \
                    + ' ' + str(self.battery_size) + "-kW"
        return long_name.title()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


"""
Styling classes.

Class names should be written in CamelCaps. Capitalize the
first letter of each word in the name, and don’t use underscores. Instance,
module and function names should be written in lowercase with underscores.

Every class should have a docstring immediately following the class definition.
Each module should also have a docstring describing what the classes in a 
module can be used for.


"""





