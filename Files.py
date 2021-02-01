# Read entire file

# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

with open('text_files/pi_digits.txt') as file_object:
    content = file_object.read()
print(content.rstrip())

print()

file = 'text_files/pi_digits.txt'
with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File
# When you use with, the file object returned by open() is only available inside the with block that contains it.
# If you want to retain access to a file’s con- tents outside the with block,
# you can store the file’s lines in a list inside the block and then work with that list.

file = 'text_files/pi_digits.txt'
with open(file) as file_object:
    obj = file_object.readlines()

for line in obj:
    print(line.rstrip())
print()
# Working with a File’s Contents

file = 'text_files/pi_digits.txt'
with open(file) as file_object:
    lines = file_object.readlines()

pi_str = ''
for line in lines:
    pi_str += line.strip()

print(pi_str)
print(len(pi_str))

# Large Files: One Million Digits

file = 'text_files/pi_million_digits.txt'
with open(file) as file_object:
    lines = file_object.readlines()

pi_str = ''
for line in lines:
    pi_str += line.strip()

print(f"{pi_str[:52]}...")
print(len(pi_str))

# Is Your Birthday Contained in Pi?

file = 'text_files/pi_million_digits.txt'
with open(file) as file_object:
    lines = file_object.readlines()

pi_str = ''
for line in lines:
    pi_str += line.strip()

birthday = input("enter birthday yyddmm: ")
if birthday in pi_str:
    print("your birthday in pi million")
else:
    print("your birthday not in pi million")

# Writing to an Empty File

file = 'text_files/programming.txt'

with open(file, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("creating new games.\n")

# Appending to a File
# If you want to add content to a file instead of writing over existing content,
# you can open the file in append mode. When you open a file in append mode, Python does’t erase the contents
# of the file before returning the file object. Any lines you write to the file will be added at the end of the file.
# If the file does’t exist yet, Python will create an empty file for you.

file = 'text_files/programming.txt'

with open(file, 'a') as file_object:
    file_object.write("I am divi.\n")
    file_object.write("creating new pro.\n")
