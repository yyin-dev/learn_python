# Try/except block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print()


# try/except/else block:
# Any code that depends on the successful execution of try block
# goes in the else block.
def divide_input():
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")

    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break

        second_number = input("Second number: ")
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by 0!")
        else:
            print(answer)


# Complete example
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("File " + filename + " has about " + str(num_words) + " words.")


filenames = ['input.txt', 'output.txt', 'nonexistent.txt', '3_dictionary.py']
for filename in filenames:
    count_words(filename)
print()


# Failing Silently
def count_words_silent(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("File " + filename + " has about " + str(num_words) + " words.")

filenames = ['input.txt', 'output.txt', 'nonexistent.txt', '3_dictionary.py']
for filename in filenames:
    count_words_silent(filename)
print()

