# Looping Through an Entire List
magicians = ['alice', 'david', 'chris']
for magician in magicians:
    # print(magician)
    print(f"{magician} that was great trick.")
    print(f"i can't wait for next trick {magician.title()}.\n ")

print("Thank you everyone, that was great magic show")

# Pizzas: Think of at least three kinds of your favorite pizza.
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['pepporoni', 'cheese', 'mushroom']

for pizza in pizzas:
    print(f"i like {pizza} pizza.")

print("i really like pizzas\n")

animals = ['cat', 'lion', 'panther']

for animal in animals:
    print(f"{animal} is in cat family")
print("only cat in three can be pet")

# Using the range() Function

for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

# using the list() function.

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 21, 2))
print(even_numbers)

print("")
# two asterisks (**) represent exponents. Here’s how you might put the first 10 square numbers into a list:

squares = []
for vale in range(1, 11):
    # square = vale ** 2
    squares.append(vale ** 2)

print(squares)

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print('')
# List Comprehensions

squaress = [value ** 2 for value in range(1, 11)]
print(squaress)

print('')
# slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:2])
print(players[:])
print(players[2:])
print(players[-3:])
print(players[1:4:2])

# Looping Through a Slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("first three players:")
for player in players[:3]:
    print(player.title())

# Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)
my_foods.append('tofu')
friend_foods.append('beans')
print("")
# two different lists
print(my_foods)
print( friend_foods)

# sometimes you’ll want to create a list of items that cannot change.Tuples allow you to do just that.
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
# Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable.
# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.
# So if we wanted to change our dimensions, we could redefine the entire tuple:

dimensions = (100, 200)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)

dimensions = (400, 300)
print("modified dimensions")
for dimension in dimensions:
    print(dimension)


