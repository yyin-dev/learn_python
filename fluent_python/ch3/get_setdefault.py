# https://tomron.net/2014/08/25/setdefault-vs-get-vs-defaultdict/
key, value = "key", "value"
data = {}
x = data.get(key, value)
print(x, data)  # value {}

data= {}
x = data.setdefault(key,value)
print(x, data) # value {'key': 'value'}
print() 

key, value = "key", "value"
data = {}
# append() modifies sequence in-place, returns None.
# get() does not modify the dictionary.
x = data.get(key, []).append(value)
print(x, data)  # None {}

data= {}
# setdefault() modifes the dictionary, and the return value is bound to the
# value of the key.
x = data.setdefault(key,[]).append(value)
print(x, data)  # None {'key': ['value']}