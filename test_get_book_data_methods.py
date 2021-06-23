import unittest
from get_book_data import list_authors_in_string, get_authors, get_title, get_publisher, get_book_to_add_search_list_number, get_list_number_for_book_replacement
from sample_test_data import test_volume

class TestGetBookDataMethods(unittest.TestCase):


    def test_list_authors_in_string(self):
        #test that list_authors_in_string properly converts author's list to a
        # string of author names separated with 'and'
        authors = ['Mark Dejon', 'Louis Elder', 'Patricia delt']
        self.assertEqual(list_authors_in_string(authors),
                         "Mark Dejon and Louis Elder and Patricia delt")
        authors = ['Mark Dejon']
        self.assertEqual(list_authors_in_string(authors),
                         "Mark Dejon")


    def test_get_authors(self):
        # Tests that get_authors retrieves the authors
        # this unfortunately relies on the list_authors_in_string function
        # there is a separate test for that function, if it fails, as will this
        self.assertEqual(get_authors(test_volume), "Dean Nicholson")


    def test_get_title(self):
        # tests that get_title retrieves the title from the volume
        self.assertEqual(get_title(test_volume), "Nala's World")


    def test_get_publisher(self):
        # tests that get_publisher retrieves the correct publisher from the vol
        self.assertEqual(get_publisher(test_volume), 'Hachette UK')


    def test_get_list_number_for_book_replacement(self):
        # I left these in here for now as a remindeer to go back and implement a
        # solution. I read up on creating a mock in order to create user input
        # to feed the input statements, such as in these two examples:
        # https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
        # https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
        # The dificulty here is that the function repeatedly asks for input
        # until a valid answer is given, therefore when the function runs
        # properly, there is no return until valid data is given on input
        # I would like to figure out the best way to approach these problems to
        # allow for proper testing
        pass


    def test_get_book_to_add_search_list_number(self):
        # please see note above, as the same applies here
        pass


if __name__ == '__main__':
    unittest.main()
