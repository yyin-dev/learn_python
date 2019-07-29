import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Use @classmethod Polymorphism to Construct Objects Generically


# Preknowledge of @staticmethod and @classmethod
# https://www.programiz.com/python-programming/methods/built-in/staticmethod
# https://www.programiz.com/python-programming/methods/built-in/classmethod
# https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod
# https://realpython.com/instance-class-and-static-methods-demystified/
#
# 1. @classmethod
# - A class method is a method bound to a class, rather than an object. It does
# not require the creation of an object. You can call the method on class. 
# - A class method, when defined, should have 'clf' as the first parameter, and 
# would be implicitly passed the class when being called. This is similar to
# to the 'self' argument for (normal/instance) methods.
# - A class method can be called both through the class or an object. 
#
# - One common use of classmethod is for constuctor overloading: Python does not
# allow multiple __init__ method for one class. However, you can manipulate
# the classmethod to do so. 

from datetime import date 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear): 
        return cls(name, date.today().year - birthYear)
        # Equivalent to:
        # Person(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()

# 2. @staticmethod
# - Staic methods, like class methods, are methods bound to class, not objects.
# - A static method does not have 'self' or 'cls': no information about the 
# class or the object is implicitly provided. It only knows the value supplied 
# as arguments. So, a static method cannot access class attributes. 
# - However, when you need a utility function that does not access attributes
# of a class, but is logically related with the class, make it a static method.
# - A static method can be called from class or object. 

class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")

# Preknowledge finished
