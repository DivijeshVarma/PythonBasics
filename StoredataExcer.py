# Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dump()
# to store this number in a file. Write a separate program that reads in this value and prints the message,
# “I know your favorite number! It’s _____.”

import json

file = 'text_files/fav_num.json'

# with open(file, 'w') as f:
#     fav_num = input("Enter your fav num: ")
#     json.dump(fav_num, f)

with open(file) as f:
    fav_num = json.load(f)
    print(f'I know your favorite number! It’s {fav_num}')

# Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number
# is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number
# and store it in a file. Run the program twice to see that it works.

file = 'text_files/favNum.json'


def get_num():
    """load fav number"""
    try:
        with open(file) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def store_num():
    """collect fav num"""
    with open(file, 'w') as f:
        fav_num = input("Enter your fav num: ")
        json.dump(fav_num, f)
        print("Thanks, I'll remember that.")


def fav_num():
    """fav num"""

    getNum = get_num()
    if getNum:
        print(f'I know your favorite number! It’s {getNum}')
    else:
        store_num()


fav_num()

# try:
#     with open('favorite_number.json') as f:
#         number = json.load(f)
# except FileNotFoundError:
#     number = input("What's your favorite number? ")
#     with open('favorite_number.json', 'w') as f:
#         json.dump(number, f)
#     print("Thanks, I'll remember that.")
# else:
#     print(f"I know your favorite number! It's {number}.")

# Verify User: The final listing for remember_me.py assumes either that the user has already entered
# their username or that the program is running for the first time. We should modify it in case the current user
# is not the person who last used the program. Before printing a welcome back message in greet_user(),
# ask the user if this is the correct username. If it’s not, call get_new_username() to get the correct username.

import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'text_files/data.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'text_files/data.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()