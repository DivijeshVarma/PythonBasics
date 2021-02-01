# Rental Car: Write a program that asks the user what kind of rental car they would like.
# Print a message about that car, such as “Let me see if I can find you a Subaru.”

car = input("what kind of rental car they would like: ")

print(f"Let me see if I can find you a {car.title()}.")

# Restaurant Seating: Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise,
# report that their table is ready.

dinner = input("how many people are in their dinner group: ")
dinner = int(dinner)

if dinner > 8:
    print("they’ll have to wait for a table")
else:
    print("your table is ready.")

# Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
# Multiples of 10 are the numbers that can be divided by 10 without any remainder.

number = input(" Enter number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple of 10")
else:
    print(f"{number} is not multiple of 10")
