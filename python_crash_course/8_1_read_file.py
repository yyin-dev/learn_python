import os
os.chdir("C:/Users/musicman/Desktop/python_learning/python_crash_course")

# Read all lines from a file
with open('input.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print("-" * 20)

"""
open() function returns an object, which we store in file_object.

The keyword with closes the file once access to it is no longer needed.
Notice we only call open() but not close() in the program. You could open
and close the file by calling open() and close(), but if a bug in your program
prevents the close() statement from being executed, the file may never close.

The only difference between this output and the original file is the
extra blank line at the end of the output. The blank line appears because
read() returns an empty string when it reaches the end of the file; this empty
string shows up as a blank line. If you want to remove the extra blank line,
you can use rstrip() in the print statement. 
"""
with open('input.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    print("-" * 20)

# Read line by line
with open('input.txt') as file_object:
    for line in file_object:
        print(line)
    """
    With this approach, you will find even more blank lines. 
    These blank lines appear because an invisible newline character is
    at the end of each line in the text file. The print statement adds its own
    newline each time we call it, so we end up with two newline characters at
    the end of each line. Using rstrip() to eliminates these extra blank lines.
    """
    print("-" * 20)

with open('input.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
    print("-" * 20)


# Making a list of lines from file
with open('input.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
    print("-" * 20)


