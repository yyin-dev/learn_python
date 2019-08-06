# List comprehension equivalent counterparts
# Example 1
squares = [x**2 for x in range(10)]

def f():
    res = []
    for x in range(10):
        res.append(x**2)
    return res

assert squares == f()

# Example 2
res = [(x, y) for x in [1, 2, 3] for y in [1, 3, 4] if x != y]

def f():
    res = []
    for x in [1, 2, 3]:
        for y in [1, 3, 4]:
            if x != y:
                res.append((x, y))
    return res
        
assert res == f()

# Example 3
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = [[row[i] for row in matrix] for i, _ in enumerate(matrix[0])]

def f():
    res = []
    for i, _ in enumerate(matrix[0]):
        res.append([row[i] for row in matrix])
    return res

def g():
    res = []
    for i, _ in enumerate(matrix[0]):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        res.append(new_row)
    return res

assert transposed == f()
assert transposed == g()
print(transposed)

# Better with zip()
smart = zip(*matrix)
for row in smart:
    print(list(row))
print(list(zip(*matrix)))


# del with list
a = [-1, 1, 66.25, 333, 333, 1234]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a 
try:
    print(a)
except Exception as e:
    print(e)


# Tuple
# Tuples are immutable, usually containing elements of different kinds that are
# accessed via unpakcing or indexing;
# List are mutable, usually containing elements of similar kinds that are
# accessed by iterating over the list.

# Syntax for constructing tuple of 0 or 1 element is special
empty_tuple = ()
single_element_tuple = "hello" ,
print(len(empty_tuple))
print(len(single_element_tuple))

# tuple packing and sequence unpacking 
nums = 1, 2, 3          # tuple packing
one, two, three = nums  # sequence unpacking
print(nums)
print(one, two, three)


# Set
# Python set can be created with curly braces: {}, or set() function. Note that
# to create an empty set, you must use set() but not {}. The latter creates
# an empty dictionary.
with_curly_braces = {'abcde'}
print(with_curly_braces)
with_set_func = set('abcde')
print(with_set_func)
print()

a = set('abcdefghi')
b = set('abcde')
print(a - b)  # in a but not b
print(a | b)  # in a, b or both
print(a & b)  # in a and b
print(a ^ b)  # in a or b, not both
# Similar to list comprehension, set comprehension is supported

intersection = {x for x in a if x in b}
assert intersection == a & b


# Dictionary
# Dictinoary keys must be immutable type. Strings and numbers can always be 
# keys. Tuples can be used as keys if they contains only strings, numbers or
# tuples. If a tuple contains any mutable object directly or indirectly, it
# cannot be used as a key.
# It's best to think of dictionary as a set of key:value pairs. Storing value
# to an existing key overwrites the original value. Extracting from an
# non-existing key raises an error.
# Calling list() returns a list of all keys used in the dictionary.
# The dict() constructor builds dictionaries from sequences of key-value pairs.
d = dict([("one", 1), ("two", 2)])
print(d)
d = dict(one=1, two=2)  # Do not use "one" or "two"
print(d)
d = dict({"one": 1, "two": 2})  # Most readable and easy to use
print(d)


# Looping techniques
# Loop through dictionary
d = dict({"one": 1, "two": 2})
for k, v in d.items():
    print(k, v)

# Loop through list with enumerate()
l = [1, 2, 3]
for element, i in enumerate(l):
    print("{}: {}".format(i, element))

# Loop through multiple sequences at the same time
questions = ['1+1', '1+2']
answers = ['2', '3']
dumb = ['bla', 'blabla']
for q, a, d in zip(questions, answers, dumb):
    print(q, a, d)

# Loop in reverse
l = [1, 2, 3]
for element in reversed(l):
    print(element)

# Be careful when changing the sequence during looping!!!


# Comparing sequences and other types
# Sequence objects can be compared to objects with the same sequence type. The
# comparison uses lexicographical ordering.
assert (1, 2, 3) < (1, 2, 4)
assert [1, 2, 3] < [1, 2, 4]
assert (1, 2) < (1, 2, -1)
assert (1, 2.0) == (1.0, 2)

# Comparing objects of different types with < or > is legal IF the objects have
# appropriate comparison methods. Thus, (1, 2.0) == (1.0, 2). Otherwise, a
# TypeError is raised. 