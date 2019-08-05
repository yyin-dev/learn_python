import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# __getattr__, getattribute__ and __setattr__ for Lazy Attributes


# If your class defines __getattr__, that method is called every time an
# attribute is cannot be found in an object's instance dictionary.
class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


data = LazyDB()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After: ', data.__dict__)


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)


data = LoggingLazyDB()
print('0     :', data.__dict__)
print('exists:', data.exists)
print('foo:   ', data.foo)
print('1:    :', data.__dict__)
print('foo:   ', data.foo)


# __getattribute__ is called every time and attribute is accessed on an object,
# even when it does exists in the attribute dictionary.
class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value


data = ValidatingDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)
print()
# You can raise AttributeError for both __getattr__ and __getattribute__

try:
    class MissingPropertyDB(object):
        def __getattr__(self, name):
            if name == 'bad_name':
                raise AttributeError('%s is missing' % name)
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

    data = MissingPropertyDB()
    data.foo  # Test this works
    data.bad_name
except Exception as e:
    print(e)
else:
    assert False

# The hasattr() is called by getattr() to check to see if AttributeError is
# to be raised or not. hasattr() is implemented by calling getattr() and see
# whether it raises an AttrubuteError or not: if the error is raised, return
# False, otherwise return True.
d = LoggingLazyDB()
print('Before:     ', d.__dict__)
print('foo exists: ', hasattr(d, 'foo'))
# The above line returns True, because the customied __getattr__ in
# LoggingLazeDB class does not throw an AttributeError.
print('After:      ', d.__dict__)
print('foo exists: ', hasattr(d, 'foo'))
print()

# Classes that implement __getattribute__ will have that method called each
# time __hasattr__ or __getattr__ is called.
data = ValidatingDB()
print('foo exists: ', hasattr(data, 'foo'))
print('foo exists: ', hasattr(data, 'foo'))
