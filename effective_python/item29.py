import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Use plain attributes instead of getters and setters


# Getter and setter makes the class cumbersome to use
class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


r0 = OldResistor(50e3)
print('Before: %5r' % r0.get_ohms())
r0.set_ohms(10e3)
print('After:  %5r' % r0.get_ohms())

r0.set_ohms(r0.get_ohms() + 5e3)


# Always begin the implementation with simple public attributes
class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
r1.ohms = 10e3
print('%r ohms, %r volts, %r amps' % (r1.ohms, r1.voltage, r1.current))
print()


# If you need special behavior when an attribute is set, use @property
# director and its corresponding setter attribute.


# Illustration how @property and @setter works:
class P:
    def __init__(self, x):
        print(self.__dict__)
        self.x = x  # Setter is called before getter. 
        # The above line can also be self.__x = x. However, calling
        # the setter method guarantees that the restriction is fulfilled. 
        print(self.__dict__)

    # This @property does not define self.x. It is just an
    # interface, like getter. As shown when printing self.__dict__.
    @property
    def x(self):
        print("Getter called")
        print(self.__dict__)
        return self.__x

    @x.setter
    def x(self, x):
        print("Setter called")
        print(self.__dict__)
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
        print(self.__dict__)

p1 = P(1001)
# print(p1.x)
print()


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = -1
        self.current = -1


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0  # setting to private: __voltage might be better

    @property
    def voltage(self):
        print("Getter called")
        return self._voltage

    # Assigning to the voltage property wuold run the setter method,
    # updating the current property.
    @voltage.setter
    def voltage(self, voltage):
        print("Setter called")
        self._voltage = voltage
        self.current = self._voltage / self.ohms
        print(self.__dict__)


r2 = VoltageResistance(1000)
print('Before: %5r amps' % r2.current)
r2.voltage = 10
print('After:  %5r amps' % r2.current)


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


try:
    res = BoundedResistance(-5)
except Exception as e:
    print(e)
    # This happens because:
    # BoundedResistance.__init__ calls Resistor.__init__, which assigns
    # self.ohms = -5. That assignment causes the @ohms.setter from
    # BoundedResistance class to be called, raising an Exception.


# Make an attributes from parent class immutable
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


fixed = FixedResistance(10)
try:
    fixed.ohms = 100
except Exception as e:
    print(e)


# Make sure that when using @property methods, the behavior of methods are not
# surprising to the user. E.g., do not set attribute in a getter method.
