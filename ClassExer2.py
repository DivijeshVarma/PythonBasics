# Dice: Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
import practice
from random import choice
from random import randint


class Die:
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)


# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)


# Lottery: Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four numbers or
# letters from the list and print a message saying that any ticket matching these four numbers or letters wins a prize.

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("\nLet's see what the winning ticket is...")

# We don't want to repeat winning numbers or letters, so we'll use a
#   while loop.
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't
    #   already been pulled.
    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)


print(f"\n4 lucky numbers {winning_ticket}\n")


# Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give you a winning ticket.

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True


def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")

# lottery 2 example

from random import randint

lot = 0
lottery_ticket = []
my_ticket = []

while len(lottery_ticket) < 4:
    lot = randint(1, 40)
    if lot not in lottery_ticket:
        lottery_ticket.append(lot)

while len(my_ticket) < 4:
    lot = int(input("enter number "))
    if lot not in my_ticket and lot <= 50 or lot > 0:
        my_ticket.append(lot)

correct = 0

for lottery in lottery_ticket:
    for ticket in my_ticket:
        if lottery == ticket:
            correct +=1

print(f"you have {correct} correct. ")
print(lottery_ticket)
print(my_ticket)

