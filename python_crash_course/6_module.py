"""
Importing functions.

You can store your functions in a separate file called a *module* and then 
import that module into your main program. 
A module is a file ending in .py that contains the code you want to import.

You can:
1. Import an entire module;
2. Import specific functions;
3. Use *as* to give a function an alias;
4. Use *as* to give a module an alias;
5. Import all functions in a Module.

Note that: Module name cannot start with number.
"""

import os
os.chdir("C:/Users/musicman/Desktop/python_learning/python_crash_course")


""" 1. Import an entire module """
import impt_src 
# import impt_src tells Python to open the file impt_src.py and copy 
# all the functions from it into this program.

impt_src.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
impt_src.dummy()


""" 2. Import specific functions """
from impt_src import make_pizza, dummy

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
dummy()


""" 3. Using as to Give a Function an Alias """
from impt_src import make_pizza as mp, dummy as dum

mp(12, 'mushrooms', 'green peppers', 'extra cheese')
dum()


""" 4. Using as to Give a Module an Alias """
import impt_src as src 

src.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
src.dummy()


""" 5. Importing All Functions in a Module """
from impt_src import * # Not a good practice
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
dummy()


"""
Importing classes.

You can:
1. Import an entire module;
2. Import specific classes;
3. Import all classes from a Module.
"""



""" 1. Import an entire module """
import impt_src

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())



""" 2. Import specific classes """

from impt_src import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())



""" 3. Import all classes from a Module """
from impt_src import *
