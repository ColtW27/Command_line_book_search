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
    global test_volume
    test_volume = {'kind': 'books#volume', 'id': 'Y1PODwAAQBAJ', 'etag': 'J5cNKR4yvjk', 'selfLink': 'https://www.googleapis.com/books/v1/volumes/Y1PODwAAQBAJ', 'volumeInfo': {'title': "Nala's World", 'subtitle': 'One man, his rescue cat and a bike ride around the globe', 'authors': ['Dean Nicholson'], 'publisher': 'Hachette UK', 'publishedDate': '2020-09-29', 'description': "**First print run only: exclusive printed endpapers showing more beautiful photographs of Dean and Nala's adventures", 'industryIdentifiers': [
        {'type': 'ISBN_13', 'identifier': '9781529328011'}, {'type': 'ISBN_10', 'identifier': '1529328012'}], 'readingModes': {'text': True, 'image': False}, 'pageCount': 272, 'printType': 'BOOK', 'categories': ['Pets'], 'maturityRating': 'NOT_MATURE', 'allowAnonLogging': True, 'contentVersion': '1.1.1.0.preview.2', 'panelizationSummary': {'containsEpubBubbles': False, 'containsImageBubbles': False}, 'imageLinks': {'smallThumbnail': 'http://books.google.com/books/content?id=Y1PODwAAQBAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api', 'thumbnail': 'http://books.google.com/books/content?id=Y1PODwAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'}, 'language': 'en', 'previewLink': 'http://books.google.com/books?id=Y1PODwAAQBAJ&dq=search_query:cat&hl=&cd=5&source=gbs_api', 'infoLink': 'http://books.google.com/books?id=Y1PODwAAQBAJ&dq=search_query:cat&hl=&source=gbs_api', 'canonicalVolumeLink': 'https://books.google.com/books/about/Nala_s_World.html?hl=&id=Y1PODwAAQBAJ'}, 'saleInfo': {'country': 'US', 'saleability': 'NOT_FOR_SALE', 'isEbook': False}, 'accessInfo': {'country': 'US', 'viewability': 'NO_PAGES', 'embeddable': False, 'publicDomain': False, 'textToSpeechPermission': 'ALLOWED', 'epub': {'isAvailable': True}, 'pdf': {'isAvailable': True}, 'webReaderLink': 'http://play.google.com/books/reader?id=Y1PODwAAQBAJ&hl=&printsec=frontcover&source=gbs_api', 'accessViewStatus': 'NONE', 'quoteSharingAllowed': False}, 'searchInfo': {'textSnippet': '**THE SUNDAY TIMES BESTSELLER** &#39;As a chronicle of an extraordinary friendship between man and animal, and its unexpected consequences, it&#39;s entirely delightful&#39; DAILY MAIL &#39;This uplifting retelling of their adventures together proves a ...'}}

        #test that list_authors_in_string properly converts author's list to a
        # string of author names separated with 'and' 
    def test_list_authors_in_string(self):
        authors = ['Mark Dejon', 'Louis Elder', 'Patricia delt']
        self.assertEqual(list_authors_in_string(authors),
                         "Mark Dejon and Louis Elder and Patricia delt")
        authors = ['Mark Dejon']
        self.assertEqual(list_authors_in_string(authors),
                         "Mark Dejon")

    def test_get_authors(self):
        self.assertEqual(get_authors(test_volume), "Dean Nicholson")


    def test_get_title(self):
        self.assertEqual(get_title(test_volume), "Nala's World")


    def test_get_publisher(self):
        self.assertEqual(get_publisher(test_volume), 'Hachette UK')


    def test_get_list_number_for_book_replacement(self):
        pass


    def test_get_book_to_add_search_list_number(self):
        pass


if __name__ == '__main__':
    unittest.main()
