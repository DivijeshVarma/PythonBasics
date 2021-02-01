# Testing a Function
import unittest
from practice import AnonymousSurvey
from practice import get_fullname

# print("enter 'q' to quit")
#
# while True:
#     first = input("Enter first name: ")
#     if first == 'q':
#         break
#     last = input("Enter last name: ")
#     if last == 'q':
#         break
#     full_name= get_fullname(first, last)
#     print(f"Formated name is {full_name}")


# Unit Tests and Test Cases
# The module unittest from the Python standard library provides tools for testing your code. A unit test verifies
# that one specific aspect of a function’s behavior is correct. A test case is a collection of unit tests that together
# prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.
# A good test case considers all the possible
# To write a test case for a function, import the unittest module and the function you want to test.
# Then create a class that inherits from unittest.TestCase, and
# write a series of methods to test different aspects of your function’s behavior.

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_fullname('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()


# Adding New Tests

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_fullname('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_fullname('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()


question = "Your fav Lan: "
mysurvey = AnonymousSurvey(question)


mysurvey.displayquestion()
print("Enter 'q' to quit")
while True:
    prompt = input('Enter: ')
    if prompt == 'q':
        break
    else:
        mysurvey.storeanswer(prompt)

print('thanks for taking survey')
mysurvey.displayresult()


class TestSurvey(unittest.TestCase):
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.storeanswer('English')
        self.assertIn('English', my_survey.survey)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.storeanswer(response)
        for response in responses:
            self.assertIn(response, my_survey.survey)


if __name__ == '__main__':
    unittest.main()


# The setUp() Method

class TestSurvey(unittest.TestCase):
    def setUp(self):
        """ Create a survey and a set of responses for use in all test methods. """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Hindi', 'Telugu']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.storeanswer(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.survey)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.storeanswer(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.survey)
