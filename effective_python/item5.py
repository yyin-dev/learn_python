""" Know How to Slice Sequences """

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

"""
Avoid being verbose: Don’t supply 0 for the start index or the length of the
sequence for the end index.
Slicing is forgiving of start or end indexes that are out of bounds, 
making it easy to express slices on the front or back boundaries of 
a sequence (like a[:20] or a[-20:]).
"""
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle two:', a[3:-3])

""" The result of slicing a list is a whole new list """
b = a[4:]
print('Before:   ', b)
b[1] = 99
print('After:    ', b)
print('No change:', a)


"""
When used in assignments, slices will replace the specified range in 
the original list. Unlike tuple assignments (like a, b = c[:2]), the length of 
slice assignments don’t need to be the same. The values before and after the 
assigned slice will be preserved. The list will grow or shrink to accommodate 
the new values
"""
print('Before ', a)
a[2:7] = [99, 22, 14]   # list shrink
print('After  ', a)
a[:2] = [1, 2, 3, 4, 5] # list grow
print('After  ', a)


""" 
If you leave out both the start and the end indexes when slicing, you’ll end 
up with a copy of the original list.
"""
b = a[:]
assert b == a and b is not a    # a and b have the same value, but are distinct


"""
If you assign a slice with no start or end indexes, you’ll replace its 
entire contents with a copy of what’s referenced (instead of allocating a 
new list).
"""
b = a
assert b == a and b is a        # a and p points to the same object
print('Before', a)
a[:] = [101, 102, 103]
assert a is b           # Still the same list object
print('After ', a)     
print('After ', b)

