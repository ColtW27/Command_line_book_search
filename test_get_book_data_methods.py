import unittest
from get_book_data import list_authors_in_string, get_authors, get_title, get_publisher, get_book_to_add_search_list_number, get_list_number_for_book_replacement


class TestGetBookDataMethods(unittest.TestCase):

    global test_volume
    test_volume = {'kind': 'books#volume', 'id': 'Y1PODwAAQBAJ', 'etag': 'J5cNKR4yvjk', 'selfLink': 'https://www.googleapis.com/books/v1/volumes/Y1PODwAAQBAJ', 'volumeInfo': {'title': "Nala's World", 'subtitle': 'One man, his rescue cat and a bike ride around the globe', 'authors': ['Dean Nicholson'], 'publisher': 'Hachette UK', 'publishedDate': '2020-09-29', 'description': "**First print run only: exclusive printed endpapers showing more beautiful photographs of Dean and Nala's adventures", 'industryIdentifiers': [
        {'type': 'ISBN_13', 'identifier': '9781529328011'}, {'type': 'ISBN_10', 'identifier': '1529328012'}], 'readingModes': {'text': True, 'image': False}, 'pageCount': 272, 'printType': 'BOOK', 'categories': ['Pets'], 'maturityRating': 'NOT_MATURE', 'allowAnonLogging': True, 'contentVersion': '1.1.1.0.preview.2', 'panelizationSummary': {'containsEpubBubbles': False, 'containsImageBubbles': False}, 'imageLinks': {'smallThumbnail': 'http://books.google.com/books/content?id=Y1PODwAAQBAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api', 'thumbnail': 'http://books.google.com/books/content?id=Y1PODwAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'}, 'language': 'en', 'previewLink': 'http://books.google.com/books?id=Y1PODwAAQBAJ&dq=search_query:cat&hl=&cd=5&source=gbs_api', 'infoLink': 'http://books.google.com/books?id=Y1PODwAAQBAJ&dq=search_query:cat&hl=&source=gbs_api', 'canonicalVolumeLink': 'https://books.google.com/books/about/Nala_s_World.html?hl=&id=Y1PODwAAQBAJ'}, 'saleInfo': {'country': 'US', 'saleability': 'NOT_FOR_SALE', 'isEbook': False}, 'accessInfo': {'country': 'US', 'viewability': 'NO_PAGES', 'embeddable': False, 'publicDomain': False, 'textToSpeechPermission': 'ALLOWED', 'epub': {'isAvailable': True}, 'pdf': {'isAvailable': True}, 'webReaderLink': 'http://play.google.com/books/reader?id=Y1PODwAAQBAJ&hl=&printsec=frontcover&source=gbs_api', 'accessViewStatus': 'NONE', 'quoteSharingAllowed': False}, 'searchInfo': {'textSnippet': '**THE SUNDAY TIMES BESTSELLER** &#39;As a chronicle of an extraordinary friendship between man and animal, and its unexpected consequences, it&#39;s entirely delightful&#39; DAILY MAIL &#39;This uplifting retelling of their adventures together proves a ...'}}


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
