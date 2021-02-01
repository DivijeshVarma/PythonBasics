# while example
number = 1

while number <= 4:
    print(number)
    number += 1

# Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ''

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
print()

# Using a Flag:gram is active. This variable, called a flag, acts as a signal to the program.
# We can write our programs so they run while the flag is set to True and stop running when any of several events
# sets the value of the flag to False. As a result, our overall while statement needs to check only one condition:
# whether or not the flag is currently True.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
print()

# Using break to exit loop
# A loop that starts with while True u will run forever unless it reaches a break statement.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'q' when you are finished.) "

while True:
    message = input(prompt)

    if message == '':
        print("don't leave blank")
    elif message == 'q':
        break
    else:
        print(f"so you visited {message}")
print()

# Using continue in a Loop
# Rather than breaking out of a loop entirely without executing the rest of its code,
# you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.
# the continue statement tells Python to ignore the rest of the loop and return to the beginning.

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)

# Avoiding Infinite Loops
# Every while loop needs a way to stop running so it won’t continue to run forever.

# x = 1
#
# while x <= 5:
#     print(x)

# Using a while Loop with Lists and Dictionaries
# Moving Items from One List to Another
# The while loop runs as long as the list unconfirmed_users is not empty.
# pop() function at removes unverified users one at a time from the end of unconfirmed_users.

unconfirmed_users = ['divi', 'rahul', 'dhoni']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"verifying {current_user}")
    confirmed_users.append(current_user)

print()
for confirmed_user in confirmed_users:
    print(f"confirmed users: {confirmed_user}")

# Removing All Instances of Specific Values from a List
# if you want to remove all instances of a value from a list?

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a Dictionary with User Input
# You can prompt for as much input as you need in each pass through a while loop.
# Let’s make a polling program in which each pass through the loop prompts for the participant’s name and response.
# We’ll store the data we gather in a dictionary, because we want to connect each response with a particular user:

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("what is your name: ")
    response = input("which mountain you would climb: ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("if any one like to take poll yes/no: ")
    if repeat == 'no':
        polling_active = False

# print dictionary values
print("\n\t--Polling Results--")
for key, value in responses.items():
    print(f"{key.title()} would like to climb {value.title()}")

