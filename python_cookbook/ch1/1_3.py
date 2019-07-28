# Keeping the Last N Items


### Preknowledge on yield
# https://stackoverflow.com/a/231855
mylist = [x * x for x in range(3)]
print(mylist)

# Print works.
for i in mylist:
    print(i)

# Print works.
for i in mylist:
    print(i)

mygen = (x * x for x in range(3))
print(mygen) # mygen is an object

# Print works
for i in mygen:
    print(i)

# Print nothing
for i in mygen:
    print(i)

def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i * i

mygen = create_generator()
# When you call the function, the code you have written in the function body does not run.
# The function only returns the generator object.
print(mygen)
for i in mygen:
    print(i)
# The first time the for calls the generator object created from your function, 
# it will run the code in your function from the beginning until it hits yield, 
# then it'll return the first value of the loop. Then, each other call will 
# run the loop you have written in the function one more time, and return 
# the next value, until there is no value to return.

# https://stackoverflow.com/a/237028/9057530
print("Preknowledge finished.")
### Preknowledge finished


from collections import deque
import os
print(os.getcwd())

# Common way of searching with generator
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line) # Append always happen, no matter pattern matches or not


# Example use on a file
if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'python_cookbook', 'ch1', 'input.txt')) as f:
        for line, prevlines in search(f, 'Hello', 5):
            print("prevlines as follows: ", len(prevlines))
            for pline in prevlines:
                # Note that as each line is from the line,
                # it automatically has a ending `\n` character
                print(pline, end="") 
            print("current line:", line, end="")
            print('-'*20)
