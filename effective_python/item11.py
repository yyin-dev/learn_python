import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

""" Use zip to Process Iterators in Parallel """

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)

""" iterate two lists in parallel with for loop """
longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)


""" Reduce visual noise slightly with enumerate() """
longest_name = None
max_letters = 0

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)

""" 
The problem with the approaches is that, we want to iterate over 2 lists 
at the same time, but we cannot easily do this and have to use index. 
Introducing index reduces the readability.
"""


""" zip() 

zip() wraps two or more iterators with a lazy generator. The zip generator 
yields tuples containing the next value from each iterator. The resulting code 
is much cleaner than indexing into multiple lists.
Note that zip behaves strangely if the input iterators are of different
lengths. It will truncates the output silently if you supply it with iterators
of different lengths.
"""
longest_name = None
max_letters = 0

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)
