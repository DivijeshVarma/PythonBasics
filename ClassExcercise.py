# Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
# that prints these two pieces of information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open. Make an instance called restaurant from your class.
# Print the two attributes individually, and then call both methods.

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")


restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# Three Restaurants: Start with your class from above  Create three different instances from the class,
# and call describe_restaurant() for each instance.

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")


mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()


# Users: Make a class called User. Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")


eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()
print()


# Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served
# with a default value of 0. Create an instance called restaurant from this class. Print the number of customers
# the restaurant has served, and then change this value and print it again. Add a method called set_number_served()
# that lets you set the number of customers that have been served. Call this method with a new number and
# print the value again. Add a method called increment_number_served() that lets you increment the number of customers
# who’ve been served. Call this method with any number you like that could represent
# how many customers were served in, say, a day of business.

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 10

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def set_number_served(self, number):
        """set the number of customers that have been served"""
        self.number_served = number

    def increment_number_served(self, number):
        """increment the number of customers"""
        self.number_served += number


restaurant = Restaurant('the mean queen', 'pizza')
print(f"{restaurant.number_served} customers restaurant has served.")

restaurant.number_served = 12
print(f"{restaurant.number_served} customers restaurant has served.")

restaurant.set_number_served(20)
print(f"{restaurant.number_served} customers restaurant has served.")

restaurant.increment_number_served(30)
print(f"{restaurant.number_served} customers were served in a day of business")


# Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.

class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def increment_login_attempts(self):
        """increments the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets the value of login_attempts to 0"""
        self.login_attempts = 0

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")


eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
print("\n3 login attempts")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f" Login Attempts: {eric.login_attempts}")

print("reset login")
eric.reset_login_attempts()
print(f" Login Attempts: {eric.login_attempts}")
print()


# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits
# from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167).
# Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores
# a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()


# Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class
# you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges()
# that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        # super(Admin, self).__init__(first_name, last_name, username, email, location)
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()


# Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a
# list of strings as described in Exercise 9-7. Move the show_privileges() method to this class.
# Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.

class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()


# Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class
# called upgrade_battery(). This method should check the battery size and set the capacity to 100 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time
# after upgrading the battery. You should see an increase in the car’s range.

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 1
        self.fill_gas = 34

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"this car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """update mileage"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("don't roll back odometer")

    def fill_gas_tank(self):
        print(self.fill_gas)

    def increment_odometer(self, miles):
        """adding miles to odometer"""
        self.odometer_reading += miles


class Battery:
    """battery related stuff"""
    def __init__(self, battery_size=34):
        self.battery_size = battery_size

    def describe_battery(self):
        """describe battery"""
        print(f"this car has a {self.battery_size} kwh battery")

    def get_range(self):
        """determine range of car"""
        if self.battery_size == 24:
            range = 200
        elif self.battery_size == 34:
            range = 330
        elif self.battery_size == 100:
            range = 500

        print(f"this car goes about {range} miles")

    def upgrade_battery(self):
        if self.battery_size == 34:
            self.battery_size = 100
            print("upgraded battery to 100")
        else:
            print("already upgraded")


class ElectricCar(Car):
    """connected with class Car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar("tesla", 'model s', 2020)
my_tesla.get_descriptive_name()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

