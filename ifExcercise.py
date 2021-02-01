# Alien Colors #1: Imagine an alien was just shot down in a game.
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green.
# If it is, print a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that fails.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.

# alien_color = 'green'
alien_color = 'yellow'
# alien_color = 'red'
if alien_color == 'green':
    print(" you've earned 5 points")
elif alien_color == 'red':
    print(" you've earned 10 points")
else:
    print(" you've earned 15 points")

# Stages of Life: Write an if- elif- else chain that determines a person’s stage of life.
# Set a value for the variable age, and then: • If the person is less than 2 years old,
# print a message that the person is a baby. • If the person is at least 2 years old but less than 4,
# print a message that the person is a toddler. • If the person is at least 4 years old but less than 13,
# print a message that the person is a kid.If the person is at least 13 years old but less than 20,
# print a message that the person is a teenager. If the person is at least 20 years old but less than 65,
# print a message that the person is an adult. If the person is age 65 or older,
# print a message that the person is an elder.

age = 23

if age < 2:
    person = 'baby'
elif 4 > age >= 2:  # age < 4 and age >= 2
    person = 'toddler'
elif 4 <= age < 13:  # age >= 4 and age < 13
    person = 'kid'
elif 13 <= age < 20:  # age >= 13 and age < 20
    person = 'teenager'
elif 20 <= age < 65:  # age >= 20 and age < 65
    person = 'adult'
else:
    person = 'elder'

print(f"\nperson is {person}")

# Favorite Fruit: Make a list of your favorite fruits,
# and then write a series of independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits. • Write five if statements.
# Each should check whether a certain kind of fruit is in your list. If the fruit is in your list,
# the if block should print a statement, such as You really like bananas!

favorite_fruits = ['apple', 'avocado', 'banana']

if 'apple' in favorite_fruits:
    print('i really like apple')
if 'grapes' in favorite_fruits:
    print('i really like grapes')
if 'banana' in favorite_fruits:
    print('i really like banana\n')

# Hello Admin: Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user: • If the username is 'admin', print a special greeting,
# such as Hello admin, would you like to see a status report? • Otherwise, print a generic greeting,
# such as Hello Jaden, thank you for logging in again.

usernames = ['divi', 'abi', 'raasi', 'admin']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user.title()}, would you like to see a status report? ")
    else:
        print(f"Hello {user.title()},  thank you for logging in again.")
print("")

# No Users: Add an if test to hello_admin.py to make sure the list of users is not empty. • If the list is empty,
# print the message We need to find some users! • Remove all of the usernames from your list,
# and make sure the correct message is printed.

# usernames = ['divi', 'abi', 'raasi', 'admin']
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report? ")
        else:
            print(f"Hello {user.title()},  thank you for logging in again.")
else:
    print("We need to find some users!\n")

# Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# Make a list of five or more usernames called current_users. • Make another list of five usernames called new_users.
# Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username.
# If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ['divi', 'abi', 'raasi', 'virat']
new_users = ['varma', 'ABI', 'jesh', 'Virat']

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user}, will need to enter a new username ")
    elif new_user == new_user.title() or new_user == new_user.upper():
        print(f"{new_user} title or upper case not accepted")
    else:
        print(f"{new_user}, username is available.")
print("")
# Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3. • Store the numbers 1 through 9 in a list.
# • Loop through the list. • Use an if- elif- else chain inside the loop to print the proper ordinal
# end- ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
# and each result should be on a separate line.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lists = list(range(1, 10))

for number in lists:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")