import io
import sys
import unittest
from print_lists import print_reading_list, print_search_results
from sample_test_data import test_search_results, crafted_book_search

# I left this here as a way to show some of my work, or at least the thpught 
# process I had for building out test cases. I unfortunately ran low on time, 
# but I was using the stack overflow post here 
# https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
# in order to capture the output of the console from a run of test data to make 
# sure it did not change. I think this is another opportunity to improve my 
# knowledge of the Unittest library on how to deal with less traditional output.
# I considered this all to be a nice learning experience in testing with the 
# built in library.

# class TestPrintListMethods(unittest.TestCase):
    
    # def test_print_search_results(self):
    #     # self.assertEqual(print_reading_list(test_search_results), )
    #     capturedOutput = io.StringIO()  # Create StringIO object
    #     sys.stdout = capturedOutput  # and redirect stdout.
    #     print_search_results(crafted_book_search)  # Call function.
    #     sys.stdout = sys.__stdout__  # Reset redirect.
    #     # print('Captured', capturedOutput.getvalue())  # Now works as before.


# if __name__ == '__main__':
#     unittest.main()
