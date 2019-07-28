import os
os.chdir("C:/Users/musicman/Desktop/python_learning/python_crash_course")

"""
The json module allows you to dump simple Python data structures into a
file and load the data from that file the next time the program runs. You can
also use json to share data between different Python programs.
"""

import json


# Basic example
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    # Dump data into json
    json.dump(numbers, f_obj)


with open(filename) as f_obj:
    # Load data back from json
    loaded_numbers = json.load(f_obj)
print(loaded_numbers)


# User greeting example
def get_stored_user(filename):
    try:
        with open(filename) as user_file:
            username = json.load(user_file)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_user(filename):
    username = input("What is your name? ")
    with open(filename, "w") as user_file:
        json.dump(username, user_file)
    return username

def greet_user(filename="user.json"):
    username = get_stored_user(filename)
    if username:
        print("Welcome back, " + username + ".")
    else:
        username = get_new_user(filename)
        print("We'll remember you when you come back, " + username + "!")

greet_user()










