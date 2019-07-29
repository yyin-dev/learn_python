import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Know How Closures Interact with Variable Scope


def sort_priority(values, group):
    """ https://stackoverflow.com/a/40962731 """
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    # 1. Functions are first-class objects in Python, meaning you can refer to 
    # them directly, assign them to variables, pass them as arguments to other 
    # functions, compare them in expressions and if statements, etc. This is 
    # how the sort method can accept a closure function as the key argument.
    # 2. Python has specific rules for comparing tuples. It first compares items
    # in index zero, then index one, then index two, and so on. This is why the
    # return value from the helper closure causes the sort order to have 
    # two distinct groups.
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True  # Seems simple
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


found = sort_priority2(numbers, group)
print('Found:', found)  # Wrong!
print(numbers)


# When you ***reference*** a variable in an expressino, Python interpreter 
# resolve names in the following order:
# 1. current function scopt;
# 2. enclosing scopt;
# 3. scope of the module, i.e. global scope;
# 4. built-in scope (that contains functions like len and str)
# If none of these places have a defined variable with the referenced name, then
# a NameError exception is raised.
#
# ***Assigning*** value to a variable works differently. If the variable is 
# already defined in the current scope, it will take on the new value. If the 
# variable doesn’t exist in the current scope, then Python treats the assignment
# as a variable definition! The scope of the newly defined variable is the 
# function that contains the assignment.
# By default, closures can’t affect enclosing scopes by assigning variables.
# This explains the behavior of the example above, called a scoping bug.
#
# Solution
# In Python 3, there is special syntax for getting data out of a closure. The 
# nonlocal statement is used to indicate that scope traversal should happen upon 
# assignment for a specific, predefined, variable name.

def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

# Avoid using nonlocal statements for anything beyond simple functions.
# When your usage of nonlocal starts getting complicated, it’s better to wrap 
# your state in a helper class. The code is longer but much more readable.

class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x): 
        """ Sorter would a callable object, like a function"""
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter) 
assert sorter.found is True
print('Found:', sorter.found)
print(numbers)