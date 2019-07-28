# Unpacking a Sequence into Separate Variables

# Any sequence (or iterable) can be unpacked into variables using a simple assignment
# operation. The only requirement is that the number of variables and structure match
# the sequence.
# If there is a mismatch in the number of elements, you’ll get an error.

p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(date)

name, shares, price, (year, mon, day) = data
print(year)


# Unpacking actually works with any object that happens to be iterable, not just tuples or
# lists. This includes strings, files, iterators, and generators.
