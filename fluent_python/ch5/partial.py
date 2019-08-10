from operator import methodcaller

space_to_underscore = methodcaller("replace", " ", "_")  # s.replace(" ", "-")
s = "Hello world"
print
print(s, "=>", space_to_underscore(s))

upper = methodcaller("upper")  # s.upper()
print(s, "=>", upper(s))


from functools import partial 
upper = partial(str.upper)  # str.upper(...)
print(s, "=>", upper(s))
