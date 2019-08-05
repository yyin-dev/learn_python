import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Reduce Visual Noise with Variable Positional Arguments


# Accepting optional positional arguments (often called star args in reference
# to the conventional name for the parameter, *args) can make a function call
# more clear and remove visual noise.

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log('My numbers are', [1, 2])
log('Hi there', [])

# Having to pass an empty list is cumbersome and noisy.
# It’d be better to leave out the second argument entirely. You can do this in
# Python by prefixing the last positional parameter name with *


def log(message, *values):  # The only difference
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log('My numbers are', 1, 2)
log('Hi there')  # Much betters

# If you already have a list and want to call a variable argument function like 
# log, you can do this by using the * operator. This instructs Python to pass 
# items from the sequence as positional arguments.

favorites = [7, 33, 99]
log('Favorite colors', *favorites)

# YY: This * operator mechanism is similar to the dereference operator in C++. 
# C++:
# int * i_ptr = new int(5); 
# int derefed = * i_ptr;
# In C++, when * is used at declaration, it means the variable is a pointer.
# When * is used on a variable that is already defined, it means dereference. 
# 
# Python:
# def func(*args):
#   for arg in args:
#       print(arg)
#
# arg_list = [1, 2, 3]
# func(*arg_list)
# When * is used at declaration, it means passed-in values will be packed into 
# a tuple. When * is used at a predefined variable(normally a tuple), it means 
# unpacking the values in the tuple.


# Two problems with accepting a variable number of position arguments. 

# The first issue is that the variable arguments are always turned into a tuple 
# before they are passed to your function. This means that if the arugment is a
# iterator produced from a generator, and the function uses * operator, then 
# it would be iterated until it is exhausted. The resulting tuple will include 
# every value from the generator, which could consume a lot of memory

def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)


# Functions that accept *args are best for situations where you know the number 
# of inputs in the argument list will be reasonably small. It’s ideal for 
# function calls that pass many literals or variable names together.

# The second issue with *args is that you can’t add new positional arguments 
# to your function in the future without migrating every caller. If you try to 
# add a positional argument in the front of the argument list, existing callers 
# will subtly break if they aren’t updated.