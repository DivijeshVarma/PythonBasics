# class example

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('roxy', 11)
your_dog = Dog('bieber', 20)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()
print()


# Working with Classes and Instances

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


# Setting a Default Value for an Attribute
# When an instance is created, attributes can be defined without being passed in as parameters.
# These attributes can be defined in the __init__() method, where they are assigned a default value.

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 1

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


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an Attribute’s Value Directly

my_new_car.odometer_reading = 24
my_new_car.read_odometer()

my_new_car.update_odometer(30)
my_new_car.read_odometer()

print()


# Incrementing an Attribute’s Value Through a Method

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 1

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

    def increment_odometer(self, miles):
        """adding miles to odometer"""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 24400
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()


# Inheritance
# You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized
# version of another class you wrote, you can use inheritance. When one class inherits from another,
# it takes on the attributes and methods of the first class. The original class is called the parent class,
# and the new class is the child class. The child class can inherit any or all of the attributes and
# methods of its parent class, but it’s also free to define new attributes and methods of its own.

# The __init__() Method for a Child Class
# When you’re writing a new class based on an existing class, you’ll often want to call the __init__() method
# from the parent class. This will initialize any attributes that were defined in the parent __init__() method
# and make them available in the child class.
# defined in that method. The name super comes from a convention of calling the parent class a superclass and
# the child class a subclass.

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

    def increment_odometer(self, miles):
        """adding miles to odometer"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """connected with class Car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 24

    def describe_battery(self):
        """describe battery"""
        print(f"this car has a {self.battery_size} kwh battery")


my_tesla = ElectricCar("tesla", 'model s', 2020)
my_tesla.get_descriptive_name()

my_tesla.describe_battery()


# Overriding Methods from the Parent Class
# You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class.
# To do this, you define a method in the child class with the same name as the method you want to override
# in the parent class. Python will disregard the parent class method and only pay attention
# to the method you define in the child class.


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


class ElectricCar(Car):
    """connected with class Car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 24

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

    def describe_battery(self):
        """describe battery"""
        print(f"this car has a {self.battery_size} kwh battery")


my_tesla = ElectricCar("tesla", 'model s', 2020)
my_tesla.get_descriptive_name()

my_tesla.describe_battery()
my_tesla.fill_gas_tank()


# Instances as Attributes

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

        print(f"this car goes about {range} miles")


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

