# Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

person = {'first_name': 'divijesh', 'last_name': 'varma', 'age': 27, 'city': 'hyderabad'}
print(person['first_name'])
print(person)

# Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person,
# and store each as a value in your dictionary. Print each person’s name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

fav_num = {'divi': 13, 'rahul': 1, 'virat': 18, 'jaddu': 8}
print(fav_num)
numb = fav_num['divi']
numb1 = fav_num['jaddu']
print(f"divi fav num is {numb}")
print(f"jaddu fav num is {numb1}")

# Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and
# then its meaning, or print the word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

prog = {'c': 'for starters',
        'python': 'easy progs',
        'java': 'experienced',
        'html': 'web devel',
        'css': 'styling'
        }

print(f"original dictionary is {str(prog)}")

for i in prog:
    print(f"{i}:")
    print(prog[i])
print()

for key, values in prog.items():
    print(f"{key}: {values}")

print()
# Rivers: Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'. • Use a loop to print a sentence about each river,
# such as The Nile runs through Egypt. • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {'ganga': 'india', 'nile': 'ezypt', 'amazon': 'brazil'}

for river in rivers:
    print(f"{river.title()} runs through {rivers[river].title()}")

for river in rivers.keys():
    print(river)

for river in rivers.values():
    print(river)
print()
# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll.
# If they have already taken the poll,print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

names = {'rahane', 'gill', 'jen', 'sarah', 'edward'}

for poll in sorted(names):
    if poll in favorite_languages.keys():
        print(f"{poll.title()}, Thanks for responding")
    else:
        print(f"{poll.title()}, you are invited for poll")

print()
# People: Make two new dictionaries representing different people, and store all three dictionaries in a list
# called people. Loop through your list of people. As you loop through the list,
# print everything you know about each person.

person_1 = {
    'first_name': 'divijesh',
    'last_name': 'varma',
    'age': 27,
}

person_2 = {
    'first_name': 'rohit',
    'last_name': 'sharma',
    'age': 32,
}
person_3 = {
    'first_name': 'shekar',
    'last_name': 'dhawan',
    'age': 33,
}
people = [person_1, person_2, person_3]

for person in people:
    for p1, p2 in person.items():
        print(f"{p1}: {p2}")
    print('--------')
print()
# Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary,
# include the kind of animal and the owner’s name. Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know about each pet.

pet_1 = {
    'name': 'sus',
    'animal': 'dog',
    'owner': 'divi',
}

pet_2 = {
    'name': 'rocky',
    'animal': 'cat',
    'owner': 'varma',
}

pets = [pet_1, pet_2]

for pet in pets:
    for p1, p2 in pet.items():
        print(f"{p1}: {p2}")
    print("-------")

# Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
# and store one to three favorite places for each person. To make this exercise a bit more interesting,
# ask some friends to name a few of their favorite places. Loop through the dictionary,
# and print each person’s name and their favorite places.

favorite_places = {
    'divi': ['bali', 'paris'],
    'virat': ['newYork', 'paris'],
    'sachin': ['london'],
}

for name, places in favorite_places.items():
    print(f"{name} favorite places are:")
    for p1 in places:
        print(f"{p1}")
print()

# Favorite Numbers: Modify your program from so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.

fav_num = {
    'divi': [13, 8],
    'rahul': [1, 100],
    'virat': [18, 28, 42],
    'jaddu': [8, 22],
}

for numb, value in fav_num.items():
    print(f"{numb}'s fav numbers are: ", end="")
    for v1 in value:
        print(v1, end=" ")
    print()

print()
# Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city. The keys for each city’s dictionary should be something
# like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'hyderabad': {
        'country': 'india',
        'population': '3M',
        'fact': 'smart',
    },
    'paris': {
        'country': 'france',
        'population': '2M',
        'fact': 'romantic',
    },
    'tokyo': {
        'country': 'japan',
        'population': '5M',
        'fact': 'developed',
    },
}

for city, info in cities.items():
    print('city: ' + city.title())
    for in1, in2 in info.items():
        print(f"{in1}: {in2}")
    print()
