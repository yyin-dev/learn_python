import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Consider Generators Instead of Returning Lists


def index_words(text):
    """ Basic example using list"""

    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.'
result = index_words(address)
print(result[:3])


# A better way to write this function is using a generator. Generators are 
# functions that use *yield* expressions. When called, generator functions do not 
# actually run but instead immediately return an iterator. With each call to 
# the next() function, the iterator will advance the generator to its 
# next yield expression. Each value passed to yield by the generator will be 
# returned by the iterator to the caller. 

# In shrot: "Generator" is a function that uses "yield", and returns a iterator 
# when it is called.

def index_words_iter(text):
    """ 
    More readable example using generator 
    The iterator returned by the generator call can easily be converted to a 
    list by passing it to the list built-in function
    """

    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
        
def index_file(handle):
    """
    The working memory for this function is bounded to the maximum length of 
    one line of input.
    """
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


address_lines="""Four score and seven years ago our fathers brought forth on this
continent a new nation, conceived in liberty, and dedicated to the proposition 
that all men are created equal."""

with open('address.txt', 'w') as f:
    f.write(address_lines)

from itertools import islice
with open('address.txt', 'r') as f:
    it = index_file(f)
    # print(list(it))
    results = islice(it, 0, 3)
    print(list(results))