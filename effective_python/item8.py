""" Avoid More Than Two Expressions in List Comprehensions """

""" Simple and readable use """
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
""" 
Read like this:
flat = [ x | for row in matrix | for x in row ], left to right, skipping x.
For each row in matrix --> for each x in this row --> put into flat.
"""
print(flat)


""" Simple and readable use """
squared = [[x**2 for x in row] for row in matrix]
print(squared)


""" Unreadable example """
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
print(flat)
""" 
At this point, the multiline comprehension isn’t much shorter than the 
alternative. The indentation of the for loop version makes the looping clearer 
than the list comprehension. 

Usage: list1.extens(list2)
The extend() extends list1 by adding all items of a list2 to the end.
"""
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
print(flat)


""" 
List comprehensions also support multiple if conditions. Multiple conditions 
at the same loop level are an implicit 'and' expression. For example, say you 
want to filter a list of numbers to only even values greater than four. 
These two list comprehensions are equivalent.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
print(b)
print(c)
assert b and c
assert b == c

""" Unreadable example """
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)

filtered = []
for row in matrix:
    if sum(row) > 10:
        filtered.append([x for x in row if x % 3 == 0])
print(filtered)

""" 
The rule of thumb is to avoid using more than two expressions in a list 
comprehension. This could be two conditions, two loops, or one condition 
and one loop. As soon as it gets more complicated than that, you should 
use normal if and for statements and write a helper function
"""
