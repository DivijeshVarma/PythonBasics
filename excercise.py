# Use a variable to represent a person’s name, and print a message to that person.
# Your message should be simple, such as, “Hello Eric,would you like to learn some Python today?”

name = 'Eric'
print(f"Hello {name}, would you like to learn some Python today?")

#  Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

name = 'divi'
print(name.lower())
print(name.upper())
print(name.title())

#  Print the quote and the name of its author. Your output should look something like the
# following, including the quotation marks:

print('Albert Einstein once said, “A person who never made a mistake never tried anything new."')

famous_person = 'Albert Einstein'
message = f"{famous_person}" + '\tonce said, “A person who never made a mistake never tried anything new."'
print(message)

# Stripping Names

name = "\n\tdivijesh\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Underscores in Numbers

universe_age = 14_000_000_000
print(universe_age)

# add ,sub, mult

print(4+4)
print(4*2)
print(16-8)
print(16/2)

# favorite number

fav_num = 13
message = "my fav num is " + f"{fav_num}"
second = "my fav num is " + str(fav_num)
print(message)
print(second)