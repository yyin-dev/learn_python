registry = []

def register(func):
    print("Running register{}".format(func))
    registry.append(func)
    return func

@register
def f1():
    print("Running f1()")

@register
def f2():
    print("Running f2()")

def f3():
    print("Running f3()")

def main():
    print("Running main()")
    print("registry:", registry)
    f1()
    f2()
    f3()
    print("registry:", registry)


if __name__ == "__main__":
    main()