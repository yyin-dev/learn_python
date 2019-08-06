# Python string is immutable, you cannot assign by index
s = "Python"
try:
    s[0] = "p"  # illegal
except Exception as e:
    print(e)
s = "python"    # legal to assign a new string


# Slice operation returns a new, distinct copy of the list
l = [1, 2, 3]
copy = l[:]
print(l == copy)
print(l is not copy)


# Multiple assignment: RHS is evaluated before any assignment
a, b = 0, 1
a, b = b, a+b
print(a, b)

def Fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a+b

print(list(Fib(10)))

