import unittest
from clean_search_query import clean_search, remove_emoji


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


if __name__ == '__main__':
    unittest.main()
