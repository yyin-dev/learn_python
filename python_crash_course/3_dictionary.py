"""
Note that in the book, the author says that python dictionary does not 
maintain the order of the elements. However, the following examples
do demonstrate that the order is maintained. 
https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6

I do not upgrade for some unstability of Python 3.7.
"""

user_0 = {
    'age': 20,
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    'gender': 'male',
}

# Loop through key-value pairs
for k, v in user_0.items():
    print("{}: {}".format(k, v))

# Loop through keys
# Looping through the keys is the default behavior for a dict.
for k in user_0.keys():
    print("{}".format(k))

for k in user_0:
    print("{}".format(k))

# Loop through values
for v in user_0.values():
    print(v)

# Loop through values, eliminate duplicates
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for language in set(favorite_languages.values()):
    print(language.title())
