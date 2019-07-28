# Finding the Largest or Smallest N Items


import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
nums = {1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2}
print(type(nums))
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

"""
Under the hood, the implementation:
1. Convert data into a list:
heap = list[nums]
2. Order items as a heap
import heapq
heapq.heapify(heap)

3. heap[0] would the smallest element. Then use heappop()
to pop off the first element and replaces it with the next smallest/largest.
With complexity: O(logN)

The nlargest() and nsmallest() functions are most appropriate if you are trying to
find a relatively small number of items. If you are simply trying to find the single smallest
or largest item (N=1), it is faster to use min() and max(). Similarly, if N is about the
same size as the collection itself, it is usually faster to sort it first and take a slice
"""
