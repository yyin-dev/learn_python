# Format strings
year = 2019
print("This is " + str(year) + " ")
print(f"This is {year}")
print("This is {}".format(year))
print("This is {input}".format(input="2019"))
print("This {0} is {1}".format("movie", "great"))
print("This {object} is {adj}".format(object="movie", adj="great"))


# Format specifier
import math
print(f"Format specifier: {math.pi:.4f}")  # Rounding happens
print("Format specifierL {:.4f}".format(math.pi))
print(f"This is {year:10}...")
print("This is {:10}...".format(year))

for x in range(1, 11):
    print("{:2d} {:3d} {:4d}".format(x, x*x, x*x*x))

for x in range(1, 11):
    # rjust() add padding space to the left. 
    # Similar methods are str.ljust(), str.center().
    # If the value is too long, a unchanged string is returned. No truncation.
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
    print(repr(x*x*x).rjust(4))

