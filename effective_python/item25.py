import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Initialize Parent Classes with super
# TLDR: Use super() for initializing the base class part in derived class.

# The old way to initialize a parent class in the __init__ method of the child 
# class is to directly call the parent class’s __init__ method.
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__(self):
        """Call parent class's __init__ directly"""
        MyBaseClass.__init__(self, 5)

    def times_two(self):
        return self.value * 2

foo = MyChildClass()
print(foo.times_two())


# However, the approach only works for simple class hierarchy and breaks down.
# One problem is: the __init__ call order isn’t specified for all subclasses.

class TimesTwo(object):
    def __init__(self):
        self.value *= 2

class PlusFive(object):
    def __init__(self):
        self.value += 5

# Diamond inheritance problem
# Diamond inheritance happens when a subclass inherits from two separate 
# classes that have the same superclass somewhere in the hierarchy.
class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5

class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)

foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but is', foo.value)
# The output should be 27 because (5 * 5) + 2 = 27. But the call to the second
# parent class’s constructor, PlusTwo.__init__, causes self.value to be reset 
# back to 5 when MyBaseClass.__init__ gets called a second time.


# Built-in function super() is introduced and defined the method resolution
# order (MRO). The MRO standardizes which superclasses are initialized
# before others (e.g., depth-first, left-to-right). It also ensures that common
# superclasses in diamond hierarchies are only run once.


# Python 2 version, much more code
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5

class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2

class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print('Seem to be (5 * 5) + 2 = 27 but is actually 5 * (5 + 2) =', foo.value)
# This order may seem backwards at first. Shouldn’t TimesFiveCorrect.__init__
# have run first? Shouldn’t the result be (5 * 5) + 2 = 27? The answer is no.
# This ordering matches rule of MRO. The MRO ordering is available on
# a class method called mro.
from pprint import pprint
pprint(GoodWay.mro())
# [<class '__main__.GoodWay'>,
#  <class '__main__.TimesFiveCorrect'>,
#  <class '__main__.PlusTwoCorrect'>,
#  <class '__main__.MyBaseClass'>,
#  <class 'object'>]

# When I call GoodWay(5), it in turn calls TimesFiveCorrect.__init__, and
# calls PlusTwoCorrect.__init__, which calls MyBaseClass.__init__. Once
# this reaches the top of the diamond(i.e. the most base class, highest in the
# hierarchy), then all of the initialization methods(i.e. constructor) are 
# invoked from the base class towards the child class.
#               BaseClass
#           /               \
#   TimesFiveCorrect    PlusTwoCorrect
#           \               /
#               GoodWay
# Just like constructor chaining in Java. The derived class's constructor can
# only be called after the base class.

# Python 2 version is not clear and requires a lot of work if you want to change
# the class hierarchy. Python 3 version is as flollows. 

class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)

class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


# Python 3
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 5

class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 2

class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super().__init__(value)


foo = GoodWay(10)
print('Should be (10 + 2) * 5 =', foo.value)

assert Explicit(10).value == Implicit(10).value