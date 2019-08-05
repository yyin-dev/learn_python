import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

""" Consider Generator Expressions for Large Comprehensions """

"""
The problem with list comprehensions is that they may create a new list 
containing one item for each value in the input sequence. The whole list
would have to be stored in memory, as the whole list is returned 
when finishing the entire evaluation.
This is fine for small inputs, but for large inputs this could
consume significant amounts of memory and cause your program to crash.

To solve this, Python provides generator expressions, a generalization of list
comprehensions and generators. Generator expressions don’t materialize 
the whole output sequence when they’re run. Instead, generator expressions 
evaluate to an iterator that yields one item at a time from the expression.
"""

import random
with open('tmp.txt', 'w') as f:
    for _ in range(5):
        f.write('a' * random.randint(0, 80))
        f.write('\n')


""" Use list comprehension """
value = [len(x) for x in open('tmp.txt')]
print(value)

""" Use generator expression to get an iterator """ 
""" 
A generator expression is created by putting list-comprehension-like syntax 
between (). The code "len(x) for x in open('my_file.txt')" is 
not executed at all. The whole expression evaluates to an iterator and doesn't
make any further progress. 
The returned iterator can be advanced one step at a time to produce the next
output from the generator expression as needed, using the next function. You
can also use the for loop to iterate with the generator for once.
"""
it = (len(x) for x in open('tmp.txt'))
print(it)
print(next(it))
print()
for e in it:
    print(e)


"""
Another powerful outcome of generator expressions is that they can be 
composed together. 
Each time you advance the outer iterator, it will also advance the interior 
iterator. Chaining generators like this executes very quickly in Python. 
"""
it = (len(x) for x in open('tmp.txt'))
roots = ((x, x*2) for x in it)
for e in roots:
    print(e)
