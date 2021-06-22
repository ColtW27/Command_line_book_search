import unittest
from clean_search_query import clean_search, remove_emoji
from get_book_data import list_authors_in_string, get_authors, get_title, get_publisher, get_book_to_add_search_list_number, get_list_number_for_book_replacement

class TestCleanSearchMethods(unittest.TestCase):

    def test_remove_emoji(self):
        #test that remove_emoji strips the emojies
        self.assertEqual(remove_emoji("Danceon😁thestreet!"),
                         "Danceonthestreet!")
        self.assertEqual(remove_emoji("🚨"),
                         "")

    def test_clean_search(self):
        #test that clean_search removes all whitespace
        self.assertEqual(clean_search("Dance!"), "Dance!")
        self.assertEqual(clean_search("Dance music"), "Dancemusic")
        self.assertEqual(clean_search(" Dance  !   music"), "Dance!music")
        self.assertEqual(clean_search(
            "    Dance    on   the street!"), "Danceonthestreet!")
        self.assertEqual(clean_search("Dance  ""   !"), "Dance!")


class TestGetBookDataMethods(unittest.TestCase):

    def test_list_authors_in_string(self):
        pass


    def test_get_authors(self):
        pass


    def test_get_title(self):
        pass


    def test_get_publisher(self):
        pass


    def test_get_book_to_add_search_list_number(self):
        pass


    def test_get_list_number_for_book_replacement(self):
        pass


if __name__ == '__main__':
    unittest.main()
