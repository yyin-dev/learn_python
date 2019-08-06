# Python scopes and namespaces
# A namespace is a mapping from names to objects. There's no relationship
# between names in different namespaces.
# The word "attribute" refers for any name following a dot.
# A scope is a textual region of a Python program where a namespace is directly
# accessible. "Directly accessible" means that an unqualified reference to a
# name attempts to find the name in the namespace.
# Scopes:
# - Innermost scope: containing local names;
# - Scope of any enclosing functions;
# - Scopt containing current module's global names;
# - Outermost scope: containing built-in names.
#
# In Python, assignments do not copy data, they just bind names to objects. The
# same is true for deletion: "del x" removes the binding of x from the
# namespace referenced by the local scope.
# The global statement can be used to indicate that particular variables live
# in the global scope and should be rebound there; the nonlocal statement 
# indicates that particular variables live in an enclosing scope and should be
# rebound there.
def scope_test():
    def local_assign():
        # Local scope. Changes local_assign()'s binding of spam.
        # Does not change scope_test()'s binding of spam.
        spam = "local"

    def nonlocal_assign():
        # Enclosing scope. Changes scope_test()'s binding of spam.
        nonlocal spam
        spam = "nonlocal"
    
    def global_assign():
        # Global scope. Changes module-level binding of spam.
        global spam
        spam = "global"
    
    spam = "test"
    local_assign()
    print(spam)
    nonlocal_assign()
    print(spam)
    global_assign()
    print(spam)

try:
    print(spam)
except Exception as e:
    print(e)
scope_test()
print(spam)
print("-"*20)


# Class
# When a class definition is entered, a new namespace is created. 
# Attribute references use the standard syntax used for all attribute
# references in Python: obj.name. Valid attribute names are all the names that
# were in the class's namespace when the class object is created.
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return "hellow world"


print(MyClass.__doc__)

x = MyClass()
print(x.f())

xf = x.f
print(xf())

print(MyClass.f)
print(x.f)
print(MyClass.f == x.f)
print("-"*20)
# x.f is a method object, but MyClass.f is a function object.

# The instance object is passed as the first argument to methods. In fact, 
# calling x.f() is exactly equivalent to MyClass.f(x). Calling a method with
# n arguments is equivalent to calling the corresponding function with (n+1)
# arguments, created from the object instance and the n arguments.


# class variables v.s. instance variables
# Instance variables are for data unique to each instance and class variables
# are for attributes and methods shared by all instances of the class.
class Dog:
    kind = "canine"     # class variable, shared

    def __init__(self, name):
        self.name = name  # instance variable, unique


# Shared data(class variable) when involving mutable objects like list or dict.
class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    

d1 = Dog("d1")
d2 = Dog("d2")
d2.add_trick("jump")
print(d1.tricks)
print(d2.tricks)
assert d1.tricks is d2.tricks
print("-"*20)


class Dog:
    def __init__(self, name):
        self.tricks = []
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    

d1 = Dog("d1")
d2 = Dog("d2")
d2.add_trick("jump")
print(d1.tricks)
print(d2.tricks)
assert d1.tricks is not d2.tricks
print("-"*20)


# Data attributes override method attributes with the same name.


print(x.__class__)
print(x.__class__.__name__)
print("-"*20)


# Inheritance
# If a requsited attribute is not found in the class, the search proceeds to
# look into the base class, recursively.
# Because methods have no special priviledges when calling other methods of the
# same object, a method of a base clas that calls another method defined in the
# base class might end up calling a method of a derived clas that overrides it.
# 
# For a method in the derived class to extend a method in the base class, simply
# call BaseClassName.methodname(self, arguments). 
# 
# Python has 2 built-in functions that work with inheritance:
# isinstance(): isinstance(obj, int)
# issubclass(): issubclass(float, int)


# Multiple inheritance
# Think of the search of attributes(Method Resolution Order) inherited from a
# parent class as depth-first, left-to-right, not searching twice in the same
# class. 


# "Private" variables
# Convention: a name prefixed with an underscore should be treated as a
# non-public part of the API and subject to change.
# Python provides limited support to avoid name clashes of names with names
# defined by subclasses, called name mangling. Any identifier of the form
# __spam(at least two leading underscores, at most one trailing underscore) is
# textually replaced with _classname__spam, where classname is the current class
# with leading underscores stripped. This mangling is done as long as the 
# identifier occurs within the definition of a class.
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


# Iterators
# for x in [1, 2, 3]: behind the scene, the for statement calls iter() on the 
# container object. Then the container object's __iter__() is invoked, which
# returns an iterator object that returns an
# iterator object that defines __next__() which acceses elements in the
# container one at a time. When there're no more elements, __next__() raises
# a StopIteration exception which tells the for loop to terminate.
s = "abc"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except Exception as e:
    print("Expected Exception")
print("-"*20)

# You can add iterator behavior to your class easily by: define an __iter__()
# method which returns an object with a __next__() method. If the class defines
# __next__(), then __iter__() can just return self.
class Iterable:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            raise StopIteration
        return self.data[self.index]
    

# Another method from Effective Python
class Iterable2:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        for d in self.data:
            yield d


it = Iterable("spam")
for item in it:
    print(item)
it = Iterable2("spam")
for item in it:
    print(item)
print("-"*20)
