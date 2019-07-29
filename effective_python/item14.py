import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

""" Prefer Exceptions to Returning None """


""" Example of possible bug in returning None """
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

assert divide(4, 2) == 2
assert divide(0, 1) == 0
assert divide(3, 6) == 0.5
assert divide(1, 0) == None

x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!
"""
Functions that return None to indicate special meaning are error prone because
None and other values (e.g., zero, the empty string) all evaluate to False in
conditional expressions.
"""


# Alternative 1: split the return value into a two-tuple
def divide(a, b):
    """ 
    The first part of the tuple indicates that the operation was a success or 
    failure. The second part is the actual result.
    """
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

x, y = 5, 0
success, result = divide(x, y)
if not success:
    print('Invalid inputs')

x, y = 5, 0
_, result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is right

x, y = 0, 5
_, result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong


""" Alternative 2(better): never return None at all and rasie an exception """
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e
""" 
The caller no longer requires a condition on the return value of the function. 
If the function didn’t raise an exception, then the return value must be good. 
The outcome of exception handling is clear.
"""
x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
