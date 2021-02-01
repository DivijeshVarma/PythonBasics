def get_fullname(first, last, middle=''):
    """format fullname"""
    if middle:
        f_name = f'{first} {middle} {last}'
    else:
        f_name = f'{first} {last}'
    return f_name.title()


# excercise

def city_country(city, country, population=''):
    """returns formated string"""
    if population:
        place = f'{city.title()}, {country.title()} - population {population}'
        return place
    else:
        place = f'{city.title()}, {country.title()}'
        return place


class AnonymousSurvey:
    """print question store answer"""

    def __init__(self, question):
        self.question = question
        self.survey = []

    def displayquestion(self):
        print(self.question)

    def storeanswer(self, prompt):
        self.prompt = prompt
        self.survey.append(self.prompt)

    def displayresult(self):
        print("results:")
        for result in self.survey:
            print(result)


class Employee:
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount
