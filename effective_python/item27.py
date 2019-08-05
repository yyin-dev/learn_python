from pprint import pprint
import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Prefer public attributes over private ones


# Basic usage
class IllustratePrivateAndPublicField(object):
    def __init__(self):
        self.public_field = 10
        self.__private_field = 20

    def get_private_field(self):
        return self.__private_field

    @classmethod
    def class_method(cls, instance):
        return instance.__private_field


obj = IllustratePrivateAndPublicField()
print(obj.public_field)
print(obj.get_private_field())
print(IllustratePrivateAndPublicField.class_method(obj))
try:
    print(obj.__private_field)
except Exception as e:
    print(e)


# Accessing private fields
class ParentClass(object):
    def __init__(self):
        self.__private_field = 10


class ChildClass(ParentClass):
    def get_parent_private_field_directly(self):
        return self.__private_field

    def get_parent_private_field_with_class(self):
        return self._ParentClass__private_field


child = ChildClass()
try:
    print(child.get_parent_private_field_directly())
except Exception as e:
    print(e)

print(child.get_parent_private_field_with_class())
print(child._ParentClass__private_field)
print("-"*20)


# Protected attribute
# Private fields cannot really preventing derived class to access attributes
# of base class. But it makes it harder to override or extend the class
# hierarchy.
class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)


class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)


foo = MyIntegerSubclass(5)  # Same as other methods, __init__ is inherited
assert foo.get_value() == 5


# The class breaks when extending the hierarchy
class MyBaseClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


class MyClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value())


class MyIntegerSubclass(MyClass):
    def get_value(self):
        # Reference to private variable is no longer valid
        return int(self._MyClass__value)


int_sub = MyIntegerSubclass(5)
try:
    print(int_sub.get_value())
except Exception as e:
    print(e)


# Use protected attribute with proper documentation is a better solution
class MyClass(object):
    def __init__(self, value):
        # This stores the user-supplied value for the object.
        # It should be coercible to a string. Once assigned for
        # the object it should be treated as immutable.
        self._value = value

    def get_value(self):
        return str(self._value)


class MyIntegerSubclass(MyClass):
    def get_value(self):
        return self._value


foo = MyIntegerSubclass(5)
print(foo.get_value())


# Seriously consider private attributes only when having naming conflict.
# For attribute names that are very common, you can use private attributes to
# reduce the risk of naming conflict.
class ApiClass(object):
    def __init__(self):
        self._value = 5

    def get(self):
        return self._value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # Conflicts


a = Child()
print(a.get(), 'and', a._value, 'should be different')


class ApiClass(object):
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # OK!


a = Child()
print(a.get(), 'and', a._value, 'are different')
