# # Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they
# # enter a 'q' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

prompt = "Enter a pizza toppings"
prompt += "\nToppings: "

while True:
    message = input(prompt)
    if message != 'q':
        print(f"I’ll add {message} topping to their pizza")
    else:
        break
print()

# # Movie Tickets: A movie theater charges different ticket prices depending on a person’s age.
# # If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;
# # and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
# # and then tell them the cost of their movie ticket.

prompt = "what is your Age: "

while True:
    message = int(input(prompt))
    if message < 3:
        print("the ticket is free")
        break
    elif message <= 12:
        print("the ticket is $10")
        break
    else:
        print("the ticket is $15")
        break

print()

# # Use a conditional test in the while statement to stop the loop.

prompt = "Enter a pizza toppings"
prompt += "\nToppings: "

exits = ''

while exits != 'q':
    message = input(prompt)
    if message != 'q':
        print(f"I’ll add {message} topping to their pizza")
    else:
        break
print()

# # Use an active variable to control how long the loop runs.

prompt = "only 2 pizza toppings are available"
prompt += "\n1st Topping: "
prompt2 = "2nd Topping: "

active = True

while active:
    message = input(prompt)
    message2 = input(prompt2)
    if message != 'q' and message2 != 'q':
        print(f"\nI’ll add {message} and {message2} toppings to your pizza")
        active = False
print()

# # Use a break statement to exit the loop when the user enters a 'q'.

prompt = "Enter a pizza toppings (or) 'q' to quit"
prompt += "\nToppings: "

while True:
    message = input(prompt)
    if message == 'q':
        break
    else:
        print(f"I’ll add {message} topping to their pizza")
print()

# # Write a loop that never ends, and run it.
#
# # x = 1
# #
# # while x <= 5:
# #     print(x)

# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and
# print a message for each order, such as I made your vegan sandwich.
# As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made,
# print a message listing each sandwich that was made.

sandwich_orders = ['tofu sandwich', 'mushroom sandwich', 'olive sandwich']
finished_sandwiches = []

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print(f"I made you {making_sandwich}.")

    finished_sandwiches.append(making_sandwich)

# listing sandwiches
print("\n--your sandwiches--")
for sandwich in finished_sandwiches:
    print(sandwich)

# Using the list sandwich_orders from above, make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and
# then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['tofu sandwich', 'pastrami', 'mushroom sandwich', 'olive sandwich', 'pastrami']
finished_sandwiches = []

print("\nthe deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print(f"I made you {making_sandwich}.")

    finished_sandwiches.append(making_sandwich)

# listing sandwiches
print("\n--your sandwiches--")
for sandwich in finished_sandwiches:
    print(sandwich)

# Dream Vacation: Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

places = {}

vacation = True

while vacation:
    poll0 = input("Enter your name: ")
    poll = input("If you could visit one place in the world, where would you go? ")
    poll2 = input("is any one want to take poll yes/no: ")

    places[poll0] = poll

    if poll2 == 'no':
        vacation = False

print("\n--Poll results--")
for key, value in places.items():
    print(f"{key.title()} would visit {value.title()}")

