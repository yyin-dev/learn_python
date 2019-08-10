from array import array
import math

class Vector2d:
    typecode = "d"

    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @classmethod
    def frombytes(cls, octets):
        # chr() returns a character from an integer
        # The first character from bytes() is the typecode
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __iter__(self):
        return (attr for attr in (self._x, self._y))

    def __repr__(self):
        classname = self.__class__.__name__
        return "{}({}, {})".format(classname, *self)

    def __str__(self):
        return "({}, {})".format(self._x, self._y)

    def __eq__(self, other):
        return self._x == other.x and self._y == other.y

    def __bytes__(self):
        return (bytes([ord(self.typecode)])) + bytes(array(self.typecode, self))

    def __abs__(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __bool__(self):
        return bool(abs(self))


v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1
print(x, y)

print(repr(v1))
v1_clone = eval(repr(v1))
print(v1 == v1_clone)

print(v1)
print(bytes(v1))

print(abs(v1))
print(bool(v1), bool(Vector2d(0, 0)))

v1.x = 4