""" Avoid Using start, end, and stride in a Single Slice """ 

"""
Python has special syntax for the stride of a slice in the form 
somelist[start:end:stride]. This lets you take every nth item when slicing 
a sequence.
"""

a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)



""" 
The point is that the stride part of the slicing syntax can be extremely 
confusing. Having three numbers within the brackets is hard enough to read 
because of its density. Also, it’s not obvious when the start and end indexes 
come into effect relative to the stride value, especially when stride is 
negative.

To prevent problems, avoid using stride along with start and end indexes. If you
must use a stride, prefer making it a positive value and omit start and end 
indexes. If you must use stride with start or end indexes, consider using 
one assignment to stride and another to slice.
"""
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b = a[::2]   # ['a', 'c', 'e', 'g']
c = b[1:-1]  # ['c', 'e']
print(a)
print(b)
print(c)