""" Use List Comprehensions Instead of map and filter """

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)


""" 
Unless you’re applying a single-argument function, list comprehensions are 
clearer than the map built-in function for simple cases. map requires creating 
a lambda function for the computation, which is visually noisy.
"""
squares = map(lambda x: x ** 2, a)
print(squares)
print(list(squares))


""" 
Unlike map, list comprehensions let you easily filter items from the input list, 
removing corresponding outputs from the result. To achieve the same effect,
you need to use map and filter together.
"""
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

""" 
Dictionaries and sets have their own equivalents of list comprehensions. 
These make it easy to create derivative data structures when writing algorithms.
"""
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)
