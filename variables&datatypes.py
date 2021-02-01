# variable

message = "hello divi!"
print(message)

# seperator

print("-------------------")

# strings

name = 'divijesh varma'
print(name.title())
print(name.upper())
print(name.lower())

# seperator

print("-------------------")

# variables in strings, f-strings, f is format
# To insert a variable’s value into a string, place the letter f 

first_name = "divijesh"
last_name = "alluri"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hi {full_name.title()}!")

message = f"hi {full_name.title()}!"
print(message)

# seperator

print("-------------------")

# Adding Whitespace to Strings with Tabs or Newlines

print("Languages: \n\tc \n\tpython \n\tjava")

# Stripping Whitespace, to eliminate extraneous whitespace from data

language = 'python '
print(language.rstrip())

# constants

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

# multiple assignment

x, y, z = 0, 1, 2
print(x, y, z)
