# Fibonacci numbers module

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

def fib2(n):
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a+b
    return res

if __name__ == "__main__":  # Runs only if the module is executed as "main"
    print("Running as __main__")
