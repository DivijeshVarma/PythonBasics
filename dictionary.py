# dictionary example
# A dictionary in Python is a collection of key-value pairs.
# Each key is connected to a value, and you can use a key to access the value associated with that key.
# A key’s value can be a number, a string, a list, or even another dictionary.

alien_0 = {'color': 'red', 'points': 6}
new_points = alien_0['points']
print(f"new points {new_points}")

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 20
print(alien_0)

# Starting with an Empty Dictionary

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 4

print(alien_1)
alien_1['color'] = 'yellow'
print(f"alien is now {alien_1['color']}")

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position of x is  {alien_2['x_position']}")
# alien_2['speed'] = 'fast'

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # must be fast alien
    x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"new position of x is {alien_2['x_position']}\n")

# removing key value pairs, deleted key-value pair is removed permanently.

alien_3 = {'color': 'pink', 'points': 7}
print(alien_3)

del alien_3['points']
print(alien_3)

# A Dictionary of Similar Objects, You can also use a dictionary to store one kind of information about many objects.

fav_langs = {
    'divi': 'python',
    'mike': 'c',
    'judy': 'java',
    'pujara': 'python'
}

language = fav_langs['divi'].title()
print(f"divi fav language is {language}")

# Using get() to Access Values, If the key 'speed' exists in the dictionary, you’ll get the corresponding value.
# If it does’t, you get the default value. In this case, speed does’t exist,
# and we get a clean message instead of an error:

alien_0 = {'color': 'red', 'points': 6}
# alien_0 = {'color': 'red', 'points': 6, 'speed': 'fast'}

speed_value = alien_0.get('speed', 'no value assigned')
print(speed_value)

# Looping Through All Key-Value Pairs

user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"Value: {value}")

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

for name, language in favorite_languages.items():
    print(f"\n{name.title()} favorite language is {language.title()}")

print("")
# Looping Through All the Keys in a Dictionary

for name in favorite_languages:
    print(name.title())

print("")
# You can access the value associated with any key you care about inside the loop by using the current key.
# Let’s print a message to a couple of friends about the languages they chose.

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

friends = ['edward', 'phil']
for name in favorite_languages:
    if name in friends:
        lang = favorite_languages[name].title()
        print(f"hi {name.title()} your fav lang is {lang} ")
    else:
        print(f"hi {name}")

if 'erin' not in favorite_languages.keys():
    print('erin take your poll')

print("")

# Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

for lang in sorted(favorite_languages.keys()):
    print(f"sorted keys {lang}")
print()

# Looping Through All Values in a Dictionary

for langs in favorite_languages.values():
    print(f"values are {langs.title()}")
print()

# To see each language chosen without repetition, we can use a set.

for langss in set(favorite_languages.values()):
    print(langss.title())
print()
# Nesting Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary.
# This is called nesting.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

alien = [alien_0, alien_1, alien_2]

for alienn in alien:
    print(alienn)
print()
# A more realistic example would involve more than three aliens with code that automatically generates each alien.
# In the following example we use range() to create a fleet of 30 aliens:

aliens = []

for alien in range(30):
    new_alien = {'color': 'green', 'speed': 'medium'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'

# top 5 aliens

for alien in aliens[:5]:
    print(alien)
print(".......")

# show how many aliens

print(f"total no of aliens is {len(aliens)}")
print()

# A List in a Dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'pepper']
}

print(f"you picked {pizza['crust']} "
      "crust and toppings are:")

for topp in pizza['toppings']:
    print(f"\t{topp}.")
print()
# You can nest a list inside a dictionary any time you want more than one value to be
# associated with a single key in a dictionary.

favorite_languages = {'jen': ['python', 'ruby'],
                      'sarah': ['c'],
                      'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'],
                      }

for name, languages in favorite_languages.items():
    print(f"{name.title()} favorite language are:")
    for language in languages:
        print(f"\t {language.title()}")
print()
#################################

favorite_languages = {'jen': ['python', 'ruby'],
                      'sarah': ['c'],
                      'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'],
                      }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()} favorite language are:")
        for language in languages:
            print(f"\t {language.title()}")
    else:
        # print(f"{name.title()} favorite language are: {languages}")
        for language in languages:
            print(f"{name.title()}'s favorite language is {language.title()} ")
print()

# A Dictionary in a Dictionary
# You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do.
# We first define a dictionary called users with two keys:usernames
# The value associated with each key is a dictionary that includes each user’s first name, last name, and location.

users = {
    'divijesh': {
        'first': 'divijesh',
        'last': 'varma',
        'location': 'india',
        },
    'kohli': {
        'first': 'virat',
        'last': 'kohli',
        'location': 'Australia',
        }
    }

for user, info in users.items():
    print(f"User: {user.title()}")
    full_name = f"{info['first']} {info['last']}"
    location = f"{info['location']}"

    print(f'\tFullname: {full_name.title()} ')
    print(f'\tLocation: {location.title()} ')
