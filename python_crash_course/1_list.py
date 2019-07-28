import copy


# Copy a list
origin = [1, 2, 3]
fake_copy = origin
origin.append(4)
print(origin)
print(fake_copy, end="\n\n")

origin = [1, 2, 3]
real_copy1 = origin[:]
real_copy2 = origin.copy()
real_copy3 = copy.copy(origin)
origin.pop()
print(origin)
print(real_copy1)
print(real_copy2)
print(real_copy3)

# Remove all instances of a value from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
