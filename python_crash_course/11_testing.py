import unittest

""" Testing function """


def get_formatted_name(first, last, middle=""):
    """Generate a neatly formatted full name."""
    if middle:  # Empty string would evaluate to False
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


# Test manually
def manual_test():
    print("Enter 'q' at any time to quit.")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == 'q':
            break
        last = input("Please give me a last name: ")
        if last == 'q':
            break

        formatted_name = get_formatted_name(first, last)
        print("\tNeatly formatted name: " + formatted_name + '.')


# Use unittest standard library
"""
A unit test verifies that one specific aspect of a function’sbehavior is 
correct. A test case is a collection of unit tests that together prove
that a functin behaves as it’s supposed to, within the full range of situations
you expect it to handle.

To write a test case for a function, import the unittest module
and the function you want to test. Then create a class that inherits from
unittest.TestCase, and write a series of methods to test different aspects of
your function’s behavior.

Any method defined within the class inheriting from unittest.TestCase 
that starts with test_ will be run automatically.
"""


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


""" Testing class """

"""
assertEqual(a, b)       Verify that a == b
assertNotEqual(a, b)    Verify that a != b
assertTrue(x)           Verify that x is True
assertFalse(x)          Verify that x is False
assertIn(item, list)    Verify that item is in list
assertNotIn(item, list) Verify that item is not in list

You can use these methods only in a class that inherits from unittest.TestCase.
"""


class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)

def anonymous_survery_manual_test():
    # Define a question, and make a survey.
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    
    # Show the question, and store responses to the question.
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == 'q':
            break
        my_survey.store_response(response)
    # Show the survey results.
    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """
        The unittest.TestCase class has a setUp() method that allows you 
        to create these objects once and use them in each of your test methods.

        When you include a setUp() method in a TestCase class, Python runs 
        the setUp() method before running each method starting with test_. That
        is, each test_ method has a new set of objects created in setUp().
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_responses(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()





