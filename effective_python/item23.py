import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Accept Functions for Simple Interfaces Instead of Classes
# 1. If the function can be stateless, never use class;
# 2. If the function have to be stateful, use a stateful closure or a class;
# 3. Class with __call__ can sometimes improve the readability.

# Functions work as hooks because Python has first-class functions: Functions
# and methods can be passed around and referenced like any other value.
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)


from collections import defaultdict
def log_missing():
    print('Key added')
    return 0

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After: ', dict(result))


# Make defaultdict count the number of missing keys with stateful hooks

# Note: the name "stateful" closure because missing() is maintaining some
# state, namely the nonlocal added_count, instead of a pure function, that
# have no variables that lives during different function calls.
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


result, count = increment_with_report(current, increments)
assert count == 2
print(dict(result))


# Make defaultdict count the number of missing keys with class
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(dict(result))


# Use __call__ to improve readibility
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()
assert callable(counter)

counter = BetterCountMissing()
result = defaultdict(counter, current)  # Relies on __call__
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(dict(result))
