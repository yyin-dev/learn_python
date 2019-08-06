# The object returned by range() behaves like a list, but is not.
# It is an object that returns the next item when you iterate over it, but
# it does not make a list, so as to save space. This kind of object is called
# iterable. The for loop is called a iterator. The function list() is another
# iterator, it creats lists from iterables.
print(range(5))
print(list(range(5)))


# The else statement for loop statements(for, while) is executed when the loop
# terminates by exhausting a list, or when the condition becomes false. It is
# not executed when the loop is terminated with a break.
# Similarly for a try statement, the else block is executed when no exception
# is raised.
for i in range(2, 10):
    for x in range(2, i):
        if i % x == 0:
            print("{} equals {} * {}".format(str(i), str(x), str(i // x)))
            break
    else:
        print("{} is a prime number.".format(str(i)))


# Function scope
s = "global"

def enclosing():
    s = "enclosing"

    def access_inner():
        s = "inner"
        print(s)
        
    def access_enclosing():
        nonlocal s
        print(s)

    def access_global():
        global s
        print(s)

    access_inner()
    access_enclosing()
    access_global()

enclosing()


# Python assignment and defintion
# https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither//
# https://www.quora.com/Are-arguments-passed-by-value-or-by-reference-in-Python
#
# Understand the mechanism
# In Python, almost everything is an object. Thus, 
# "variables" should be more properly called "names", and "assignment" should
# be more properly called "binding a name to an object". Each binding has a 
# scope, usually within that function block.
# C++:
# string some_guy = "Fred";
# some_guy = "George";
# In the code above, variable name refers to a memory location. At definition, 
# "Fred" is inserted into that location. At assigning, "George" overwrites the
# original value("Fred").
# 
# Python works differently:
# some_guy = "Fred"     (1)
# some_guy = "George"   (2)
# Line (1) creates a binding between name some_guy and string object containing 
# "Fred". At line (2), the name some_guy is bound to another string object
# containing "George", but the original string object "Fred" is unaffected. We 
# are just changing the binding of the name, but not changing the string
# objects.
some_guy = 'Fred'  # a string object created and bound to some_guy

first_names = []  # an empty list created and bound to first_names
first_names.append(some_guy)  # list bound to first_names changed

# Assignment between names does not create new objects. 
# another_list_of_names will bind to the same object as first_names.
# The two names bind to the same list object.
another_list_of_names = first_names  
assert another_list_of_names == first_names
assert another_list_of_names is first_names
another_list_of_names.append('George')
some_guy = 'Bill'

print (some_guy, first_names, another_list_of_names)

# There are 2 kinds of objects. A mutable object has time-varying behavior.
# Changes to a mutable object are visible through all names bound to it. An 
# immutable object does not exhibit time-varying behavior. The value of 
# immutable objects CANNOT be modified after they are created. Everything is 
# an object in Python. If integers were not immutable I could change the 
# meaning of the number '2' throughout my program.

# Legal usage:
first_names = ['Fred', 'George', 'Bill']
last_names = ['Smith', 'Jones', 'Williams']
name_tuple = (first_names, last_names)  # tuple is immutable

first_names.append('Igor')


# If I call foo(bar), I'm merely creating a binding within the scope of foo to
# the object the argument bar is bound to. If bar refers to a mutable object 
# and foo changes its value, then these changes will be visible outside of 
# the scope of the function. If bar refers to an immutable object, foo can at 
# most create a name bar in its local namespace and bind it to other object.

# Passing name referring to mutable object
def foo(lst):
    lst.append(42)
    print(lst)

l = []
foo(l)  # parameter 'lst' would refer to the same object as 'l'
print(l)

# Passing name referring to immutable object
def bar(input_s):
    input_s = 'new value'  
    # name 'input_s' bound to another object. Orignial object is unaffected.

    print (input_s)
    try:
        input_s[0:3] = "NEW"
    except Exception as e:
        print(e)

s = 'old value'
bar(s)  # parameter 'input_s' would refer to the same object as 's'
print(s)


# Python symbol table
# https://www.programiz.com/python-programming/methods/built-in/globals
# A function definition introduces the function name in the current symbol
# table. The value of the function name has a type of user-defined function. 
# This value can be assigned to another name, which can also be used as a
# function.
print(Fib)
fibnacci = Fib
print(fibnacci)  # referring to the same object
# In Python, functions without return statements implicitly returns None.


# Default value for function is evaluated only once, at definition
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In a function call, keyword arguments must follow positional arguments.


# *args and **kwargs
def illustrate(first, *args, **kwargs):
    for arg in args:
        print(arg)
    print("-"*20)
    for k in kwargs:
        print("{}: {}".format(k, kwargs[k]))
    
illustrate("first_arg", "hello", "world", hello="hello", world="world")


# Use lambda for small anonymous functions
def get_incrementor():
    return lambda x: x + 1

incrementor = get_incrementor()
print(incrementor(5))


# Function annotations are completely optional metadata info about the types
# used by user-defined functions
def f(ham: str, eggs: str = "eggs") -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs

print(f("spam"))
