from pprint import pprint
import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Use Multiple Inheritance Only for Mix-in Utility Classes [Difficult, skipped]

# Base class ordering:
# https://www.georgevreilly.com/blog/2016/01/14/PythonBaseClassOrder.html


class Useful(object):
    def __init__(self):
        super().__init__()
        print("Useful.__init__")

    def stuff(self):
        print("useful stuff")


class Mixin(object):
    def __init__(self):
        super().__init__()
        print("Mixin.__init__")

    def stuff(self):
        print("mixin stuff")


class UsefulThenMixin(Useful, Mixin):
    def __init__(self):
        super().__init__()
        print("UsefulThenMixin.__init__")


class MixinThenUseful(Mixin, Useful):
    def __init__(self):
        super().__init__()
        print("MixinThenUseful.__init__")


# The sequence of initialization call(__init__) is opposite to methods
pprint(UsefulThenMixin.mro())
pprint(MixinThenUseful.mro())
obj = UsefulThenMixin()
obj = MixinThenUseful()

UsefulThenMixin().stuff()
MixinThenUseful().stuff()
