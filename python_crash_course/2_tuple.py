"""
Python list is for storing items changable throughtout the
lifespan. 
Tuple is used for storing unchangable items. That is,
python tuple is immutable. 
"""

dimensions = (100, 50)
print(dimensions[0], dimensions[1])

try:
    dimensions[0] = 200
except Exception as e:
    print("Exception catched! {}".format(e))

"""
Although you cannot modify the elements in a tuple, you 
can assign a new value to the variable holding the tuple.
"""

print("Original dimensions: {}".format(dimensions))
dimensions = (200, 100)
print("Modified dimensions: {}".format(dimensions))



