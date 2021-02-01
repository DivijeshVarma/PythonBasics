# Exceptions
# We put print(5/0), the line that caused the error, inside a try block. If the code in a try block works,
# Python skips over the except block. If the code in the try block causes an error, Python looks for an except block
# whose error matches the one that was raised and runs the code in that block.

try:
    print(5/0)
except ZeroDivisionError:
    print("can't divide by zero")

# Using Exceptions to Prevent Crashes

print("enter 2 numbers i will divide them")
print("enter 'q' to quit")

while True:
    f_num = input("number1: ")
    if f_num == 'q':
        break

    l_num = input("number2: ")
    if l_num == 'q':
        break
    try:
        div = int(f_num)/int(l_num)
    except ZeroDivisionError:
        print("can't divide by zero\n")
    else:
        print(f'Result: {div}\n')

# Handling the FileNotFoundError Exception

file = 'text_files/proogramming.txt'

try:
    with open(file) as f:
        print(f.read())
except FileNotFoundError:
    print(f"file {file} not found")


# Analyzing Text
# The split() method separates a string into parts wherever it finds a space and stores all the parts of the
# string in a list. The result is a list of words from the string,
# Using the try- except block in this example provides two significant advantages.
# We prevent our users from seeing a traceback, and we let the program continue analyzing the texts it’s able to find.
# If we don’t catch the FileNotFoundError that siddhartha.txt raised, the user would see a full traceback, and
# the program would stop running after trying to analyze Siddhartha. It would never analyze Moby Dick or Little Women.

def count_words(file):
    try:
        with open(file) as f:
            words = f.read()
    except FileNotFoundError:
        print(f"file {file} not found")
    else:
        words = words.split()
        print(f'{file} has about {len(words)} words')


# file = 'text_files/programming.txt'
# count_words(file)

files = ['text_files/guest.txt', 'text_files/pi_ddigits.txt', 'text_files/programming.txt']

for file in files:
    count_words(file)
print()


# Failing Silently
# Sometimes you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened.
# To make a program fail silently, you write a try block as usual

def count_words(file):
    try:
        with open(file) as f:
            words = f.read()
    except FileNotFoundError:
        pass
    else:
        words = words.split()
        print(f'{file} has about {len(words)} words')


# file = 'text_files/programming.txt'
# count_words(file)

files = ['text_files/guest.txt', 'text_files/pi_ddigits.txt', 'text_files/programming.txt']

for file in files:
    count_words(file)
