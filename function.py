# function

def greet_user():
    """greeting user"""
    print("hello")


greet_user()


# Passing Information to a Function
# The variable user in the definition of greet_user() is an example of a parameter,
# a piece of information the function needs to do its job.
# The value 'varma' in greet_user('varma') is an example of an argument.
# An argument is a piece of information that’s passed from a function call to a function.
# When we call the function, we place the value we want the function to work with in parentheses.
# In this case the argument 'varma' was passed to the function greet_user(),
# and the value was assigned to the parameter user.

def greet_user(user):
    """greeting user"""
    print(f"hello {user}")


greet_user('varma')


# Positional Arguments

def pets(types, name):
    """display info about pet"""
    print(f"pet: type-{types}, name-{name}")


pets('cat', 'ruby')
pets(types='dog', name='snoopy')


# Default Values

def pets(name, types='dog'):
    """display info about pet"""
    print(f"pet: type-{types}, name-{name}")


pets('cat', 'ruby')
pets(name='snoopy')


# Default Valuess

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie', animal_type='cat')

print()


# Return Values A function does’t always have to display its output directly.
# Instead, it can process some data and then return a value or set of values.
# The value the function returns is called a return value.
# The return statement takes a value from inside a function and sends it back to the line that called the function.
# Return values allow you to move much of your program’s grunt work into functions,
# which can simplify the body of your program.

def format_name(f_name, l_name):
    """Return a full name, neatly formatted."""
    full_name = f"{f_name} {l_name}"
    return full_name.title()


message = format_name('divijesh', 'varma')
print(message)

print()


# Making an Argument Optional

def format_name(f_name, l_name, m_name=''):
    """Return a full name, neatly formatted."""
    if m_name:
        full_name = f"{f_name} {m_name} {l_name}"
    else:
        full_name = f"{f_name} {l_name}"

    return full_name.title()


message = format_name('divijesh', 'alluri', 'varma')
message2 = format_name('divijesh', 'alluri')
print(message)
print(message2)

print()


# Returning a Dictionary

def format_name(f_name, l_name):
    """Return a full name, neatly formatted."""
    full_name = {'first': f_name, 'last': l_name}
    return full_name


message = format_name('divi', 'varma')
print(message)


# adding to dictionary
# value. In conditional tests, None evaluates to False.
# If the function call includes a value for age, that value is stored in the dictionary. This function

def for_name(f_name, l_name, age=None):
    full_name = {'first': f_name, 'last': l_name}
    if age:
        full_name['age'] = age
    return full_name


message = for_name('divi', 'varma', 27)
print(message)


# Using a Function with a while Loop

# def format_name(f_name, l_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{f_name} {l_name}"
#     return full_name.title()


# # infinite loop
# while True:
#     print("\nTell me your name")
#     fi_name = input('first_name: ')
#     la_name = input('last_name: ')
#     ful_name = format_name(fi_name, la_name)
#     print(f"\nhello {ful_name}")


# quit infinite loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


# Passing a List

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
# Consider a company that creates 3D printed models of designs that users submit.
# Designs that need to be printed are stored in a list, and after being printed they’re moved to a separate list.
# The following code does this without using functions:

unprinted_designs = ['phone', 'dode', 'facts']
completed_models = []

while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print(f"current designs {current_designs}")
    completed_models.append(current_designs)

print("\ncompleted models:")
for completed_model in completed_models:
    print(completed_model)


# We can reorganize this code by writing two functions, each of which does one specific job.
# Most of the code won’t change; we’re just making it more carefully structured.
# The first function will handle printing the designs, and the second will summarize the prints that have been made:
# This example also demonstrates the idea that every function should have one specific job.
# The first function prints each design, and the second displays the completed models.
# This is more beneficial than using one function to do both jobs.
# If you’re writing a function and notice the function is doing too many different tasks,
# try to split the code into two functions. Remember that you can always call a function from another function,
# which can be helpful when splitting a complex task into a series of steps.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(f"{unprinted_designs}\n")


# But because you moved all the design names out of unprinted_designs, the list is now empty, and
# the empty list is the only version you have; the origi- nal is gone. In this case, you can address this issue by
# passing the function a copy of the list, not the original. Any changes the function makes to the list will affect only
# the copy, leaving the original list intact.
# You can send a copy of a list to a function like this:
# function_name(list_name[:])

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(f"{unprinted_designs}\n")


# Passing an Arbitrary Number of Arguments
# The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and
# pack whatever values it receives into this tuple.

def make_pizza(*toppings):
    """print requested toppings"""
    print(toppings)


make_pizza('mushroom')
make_pizza('ppp')
make_pizza('mushroom', 'cheese', 'pepperoni')


# loop through toppings

def make_pizza(*toppings):
    """print requested toppings"""
    print("\nmake following toppings")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza('mushroom')
make_pizza('mushroom', 'cheese', 'peppromi')


# Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings):
    """print requested toppings"""
    print(f"\nthe size is {size}-inch and following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza(9, 'mushroom')
make_pizza(10, 'mushroom', 'cheese', 'pepperoni')


# Using Arbitrary Keyword Arguments
# double asterisks before the parameter **user_info cause Python to create
# an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.


def build_profile(first, last, **profile):
    profile['first'] = first
    profile['last'] = last
    return profile


user_profile = build_profile('Albert', 'Einstein', location='princeton', field='physics')
print(user_profile)


