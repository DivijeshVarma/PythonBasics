# Simple example

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

pizza_toppings = 'mushrooms'

if pizza_toppings != 'pickels':
    print('\nselect pickels')

answer = 22

if answer != 24:
    print('\nwrong answer')

# Checking Whether a Value Is Not in a List

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
user2 = 'david'

if user not in banned_users:
    print('\nyou are not banned')

if user2 in banned_users:
    print('\nyou are banned')

# Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print('')
# using keyword and, or

food = 'tofu'
if food == 'tofu' and food == 'cream':
    print('correct')
else:
    print('wrong')

if food == 'tofu' or food == 'cream':
    print('correct')
else:
    print('wrong')

# conditional test

age = 19

if age >= 18:
    print("you're old enough to vote ")
else:
    print("you're too young to vote")

# The if-elif-else Chain
# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $25.
# Admission for anyone age 18 or older is $40.

age = 9

if age < 4:
    print("admission fee is $0")
elif age <= 18:
    print("admission fee is $25")
else:
    print("admission fee is $40")

# it would be more concise to set just the price inside the if- elif- else chain and
# then have a simple print() call that runs after the chain has been evaluated:

age = 11

if age < 4:
    price = 0
elif age <= 18:
    price = 25
else:
    price = 40

print(f"admission fee is ${price}")

# Testing Multiple Conditions The if- elif- else chain is powerful,
# but it’s only appropriate to use when you just need one test to pass.
# As soon as Python finds one test that passes, it skips the rest of the tests.
# This code would not work properly if we used an if- elif- else block,
# because the code would stop running after only one test passes.


print("")
requested_toppings = ['mushrooms', 'olives']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
if 'tofu' in requested_toppings:
    print("adding tofu")
if 'olives' in requested_toppings:
    print("adding olives")

print("pizza ready\n")

# Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("green peppers not available")
    else:
        print(f"adding {requested_topping}")

print("\nfinished making your pizza.\n")

# Checking That a List Is Not Empty
# Python returns True if the list contains at least one item; an empty list evaluates to False.
# If requested_toppings passes the conditional test, we run the same for loop we used in the previous example.
# If the conditional test fails, we print a message asking the customer
# if they really want a plain pizza with no toppings

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}")
    print("pizza ready")
else:
    print("are you sure want plain pizza?\n")

# Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding{requested_topping}")
    else:
        print(f"sorry {requested_topping} not available")

print("\npizza ready")