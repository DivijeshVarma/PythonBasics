# Store the names of a few of cities in a list called names. Print
# each cities name by accessing each element in the list, one at a time.

names = ['hyderabad', 'london', 'sydney', 'new york', 'toronto']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#  print a message to them. The text of each message should be the same,
#  but each message should be personalized with the city name.
message = f"my favorite city {names[0].title()}"
message1 = f"my favorite city {names[1].title()}"
message2 = f"my favorite city {names[2].title()}"
message3 = f"my favorite city {names[3].title()}"
message4 = f"my favorite city {names[4].title()}"
print(message)
print(message1)
print(message2)
print(message3)
print(message4)

# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

dinner_invite = ['mahi', 'virat', 'dravid']
print(f"\ninvitation for dinner {dinner_invite[0]}")
print(f"invitation for dinner {dinner_invite[1]}")
print(f"invitation for dinner {dinner_invite[2]}")

# Changing Guest List: You just heard that one of your guests can’t make the dinner,
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

not_coming = 'mahi'
dinner_invite.remove(not_coming)
print(f"{not_coming} can't make the dinner")
dinner_invite.insert(0, 'sachin')
print(f"\ninvitation for dinner {dinner_invite[0]}")
print(f"invitation for dinner {dinner_invite[1]}")
print(f"invitation for dinner {dinner_invite[2]}")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.

print(f"\nfound out bigger dinner table, adding 3 more guests {dinner_invite[0]}")
print(f"found out bigger dinner table, adding 3 more guests {dinner_invite[1]}")
print(f"found out bigger dinner table, adding 3 more guests {dinner_invite[2]}")

print(len(dinner_invite))

dinner_invite.insert(0, 'anushka')
dinner_invite.insert(2, 'sehwag')
dinner_invite.append('yuvraj')

print(f"new invitation for dining {dinner_invite[0]}")
print(f"new invitation for dining {dinner_invite[1]}")
print(f"new invitation for dining {dinner_invite[2]}")
print(f"new invitation for dining {dinner_invite[3]}")
print(f"new invitation for dining {dinner_invite[4]}")
print(f"new invitation for dining {dinner_invite[5]}")

# 3-7. Shrinking Guest List: You just found out that your new dinner table
# won’t arrive in time for the dinner, and you have space for only two guests.

print(" only 2 people invited ")
name = dinner_invite.pop()
print(f"\nsorry we can't invite to dinner {name}")
name = dinner_invite.pop()
print(f"sorry we can't invite to dinner {name}")
name = dinner_invite.pop()
print(f"sorry we can't invite to dinner {name}")
name = dinner_invite.pop()
print(f"sorry we can't invite to dinner {name}")

print(f"your still invited {dinner_invite[-1]}")
print(f"your still invited {dinner_invite[-2]}")

del dinner_invite[0]
del dinner_invite[0]

print(dinner_invite)
print(len(dinner_invite))

# Seeing the World: Think of at least five places in the world you’d like to visit.
print('')
vacation_list = ['dubai', 'singapore', 'amsterdam', 'paris', 'new york']
print(vacation_list)
print(sorted(vacation_list))
print(vacation_list)
print(sorted(vacation_list, reverse=True))
print(vacation_list)
vacation_list.reverse()
print(vacation_list)
vacation_list.reverse()
print(vacation_list)
vacation_list.sort()
print(vacation_list)
vacation_list.sort(reverse=True)
print(vacation_list)

# Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for value in range(1, 21):
    print(value)

# Make a list of the numbers from one to 100, and then use a for loop to print the numbers.
lists = list(range(1, 100))
# print(lists)
for value in lists:
    print(value)

print("")
# Summing a 100: Make a list of the numbers from one to 100, and then use min() and max()
# to make sure your list actually starts at one and ends at 100.
# Also, use the sum() function to see how quickly Python can add a 100 numbers.

numbers = list(range(1, 101))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("")
# Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.

odd_numbers = list(range(1, 20, 2))
for value in odd_numbers:
    print(value)

print("")
# Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

for valle in range(3, 31):
    multiple = valle * 3
    print(multiple)

multiply = [val * 3 for val in range(3, 31)]
print(multiply)

print("")
# Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
# and use a for loop to print out the value of each cube.

for vals in range(1, 11):
    cubes = vals ** 3
    print(cubes)

cube = [val ** 3 for val in range(1, 11)]
print(cube)

# Print the message The first three items in the list are:. Then use a slice to print the first three items from that
# program’s list. Print the message Three items from the middle of the list are:. Use a slice to print three items
# from the middle of the list. Print the message The last three items in the list are:. Use a slice to print the last
# three items in the list.

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# players_slice = players[:3]
print(f"The first three items in the list are: {players[:3]}")
print(f"Three items from the middle of the list are: {players[2:]}")
print(f"The last three items in the list are: {players[-3:]}")

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of
# pizzas, and call it friend_pizzas. Then, do the following: Add a new pizza to the original list. Add a different
# pizza to the list friend_pizzas. Prove that you have two separate lists. Print the message My favorite pizzas are:,
# and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:,and then use a
# for loop to print the sec- ond list. Make sure each new pizza is stored in the appropriate list.

pizzas = ['pepporoni', 'cheese', 'mushroom']
friend_pizzas = pizzas[:]
pizzas.append('chilli')
friend_pizzas.append('tofu')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are: ")
for fpizza in friend_pizzas:
    print(fpizza)

# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple. Use
# a for loop to print each food the restaurant offers. Try to modify one of the items, and make sure that Python
# rejects the change. The restaurant changes its menu, replacing two of the items with different foods. Add a line
# that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

foods = ('noodles', 'tofu', 'broccoli', 'pizza', 'ice_cream')
print('\nrestaurant offers:')
# foods[0] = ('beans')
for food in foods:
    print(food)

print('replacing 2 items:')
foods = ('noodles', 'tofu', 'quinoa', 'pizza', 'asparagus')
for food in foods:
    print(food)
