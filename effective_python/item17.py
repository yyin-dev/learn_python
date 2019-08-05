import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Be Defensive When Iterating Over Arguments


# Iterate over the list argument
def normalize(numbers):
    # sum() function iterates over the argument, which must be an iterable.
    # Thus, if the argument is a generator, then the iterator is exhausted after
    # sum(). However, no exception would be raised.
    total = sum(numbers)  # iterate protocol in effect
    result = []
    for value in numbers:  # iterate protocol in effect
        percent = 100 * value / total
        result.append(percent)
    return result


# Works when passing into a list
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


# To scale up, rewrite using generator
path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)

it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))  # Already exhausted


# Surprisingly, calling normalize() on the generator’s return value produces no
# results. The cause is that an iterator produces its results only once.
# If you iterate over an iterator or generator that has already raised a
# StopIteration exception, you won’t get any results the second time around.
#
# What’s confusing is that you also won’t get any errors when you iterate over
# an already exhausted iterator. For loops, list constructors and other Python
# functions cannot tell the difference between an iterator that has no output
# and an iterator that had output but is exhausted.
#
# To solve this problem, you can explicitly exhaust an input iterator and keep
# a copy of its entire contents in a list. You can then iterate over the
# list version of the data as many times as you need to.


def normalize_copy(numbers):
    numbers = list(numbers)  # Copy the iterator into a list
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)


# The problem with this approach is the copy of the input iterator’s contents
# could be large. Copying the iterator could cause your program to run out of
# memory and crash.
#
# A better way: implement the *iterator protocol*.
# The iterator protocol is how Python for loops and related expressions
# traverse the contents of a container type. When Python sees a statement that
# expects a iterable, like: for x in foo, it calls iter(foo). The iter()
# function calls the foo.__iter__ special method in turn. The __iter__ method
# must return an iterator object (which itself implements the __next__ special
# method). Then the for loop repeatedly calls the next built-in function on
# the iterator object until it’s exhausted and raises StopIteration exception.
#
# for x in foo/ sum(foo):
#   -> iter(foo)
#   -> foo.__iter__ (returns an iterator implmenting __next__)
# Then iterate over the returned iterator object.
#
# Practically speaking, you can achieve all of this behavior for your classes
# by implementing the __iter__ method as a generator(i.e. using yield).


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
# This works because the sum method in normalize will call
# ReadVisits.__iter__ to allocate a new iterator object. The for loop to
# normalize the numbers will also call __iter__ to allocate a second iterator
# object. Each of those iterators will be advanced and exhausted independently,
# ensuring that each unique iteration sees all of the input data values. The
# only downside of this approach is that it reads the input data multiple times.


# You might also employ type check to ensure that parameters aren't just
# iterators. The protocol states that when an iterator is passed to the iter()
# built-in function, iter will return the iterator itself. In
# contrast, when a container type is passed to iter, a new iterator object will
# be returned each time.


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # Checking if input is iterator
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
normalize_defensive(visits)  # No error
visits = ReadVisits(path)
normalize_defensive(visits)  # No error


def normalize_defensive_with_generator(numbers):  # From item 16
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError('Must supply a container')

    total = sum(numbers)
    for value in numbers:
        percent = 100 * value / total
        yield percent


print(list(normalize_defensive_with_generator(visits)))
