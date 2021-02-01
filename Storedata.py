# Storing Data
# The json module allows you to dump simple Python data structures into a file and load the data from that file
# the next time the program runs. You can also use json to share data between different Python programs.
# Using json.dump() and json.load()
# The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data.
# Here’s how you can use json.dump() to store a list of numbers:

import json

numbers = [2, 3, 6, 7, 8, 10]

file = 'text_files/numbers.json'

with open(file, 'w') as f:
    json.dump(numbers, f)


file = 'text_files/numbers.json'

with open(file) as f:
    num = json.load(f)

print(num)

file = 'text_files/numbers.json'

prompt = input(" Enter your name: ")

with open(file, 'w') as f:
    json.dump(prompt, f)

file = 'text_files/numbers.json'

with open(file) as f:
    data = json.load(f)
    print(data)

# We need to combine these two programs into one file. When someone runs remember_me.py, we want to retrieve
# their username from memory if possible; therefore, we’ll start with a try block that attempts to recover the username.
# If the file username.json doesn’t exist, we’ll have the except block prompt
# for a username and store it in username.json for next time:

import json

filename = 'text_files/data.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")


# Refactoring Often, you’ll come to a point where your code will work, but you’ll recognize that
# you could improve the code by breaking it up into a series of functions that have specific jobs.
# This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend.

def greet_user():
    """greet user"""
    filename = 'text_files/data.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")


greet_user()


# but the function greet_user() is doing more than just greeting the user—it’s also retrieving a stored username
# if one exists and prompting for a new username if one doesn’t exist. Let’s refactor greet_user()
# so it’s not doing so many different tasks. We’ll start by moving the code for retrieving a stored username
# to a separate function:

def store_username():
    """store username"""
    file = 'text_files/datas.json'
    try:
        with open(file) as f:
            rd = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return rd


def greet_user():
    """greet user"""
    user = store_username()
    if user:
        print(f'welcome {user}')
    else:
        user = input('Enter username: ')
        file = 'text_files/datas.json'
        with open(file, 'w') as f:
            json.dump(user, f)


greet_user()


# Each function in this final version of remember_me.py has a single, clear purpose. We call greet_user(),
# and that function prints an appropriate message: it either welcomes back an existing user or greets a new user.
# It does this by calling get_stored_username(), which is responsible only for retrieving
# a stored username if one exists. Finally, greet_user() calls get_new_username() if necessary,
# which is responsible only for getting a new username and storing it. This compartmentalization of work
# is an essential part of writing clear code that will be easy to maintain and extend.

def store_usernamee():
    """store username"""
    file = 'text_files/data.json'
    try:
        with open(file) as f:
            rd = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return rd


def create_user():
    """create user"""
    user = input('Enter username: ')
    file = 'text_files/data.json'
    with open(file, 'w') as f:
        json.dump(user, f)
    return user


def greet_user():
    """greet user"""
    user = store_usernamee()
    if user:
        print(f'welcome {user}')
    else:
        c_u = create_user()
        print(f'well get back {c_u}')


greet_user()