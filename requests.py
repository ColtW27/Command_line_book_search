import json  # built in module for json data
from urllib.request import urlopen  # Python built-in module for opemning and reading URLS

# create variable to house the api and search query
api = "https://www.googleapis.com/books/v1/volumes?q=search_query:"
search_queury = input(f"Please enter your search \n ") #.strip()

# send a restful request and receives the response as JSON. This is the entire
response = urlopen(api + search_queury)
# Allows the parsing and conversion of JSON into Python
book_search_response = json.load(response)  # Represents the entire object and data on search
book_items_list = book_search_response["items"] # Items array that holds the volumes (books)
first_book = book_items_list[0]
# print(book_data["items"][0]['volumeInfo']["title"])
# print(first_book)

reading_list = []  # this can only have 5 items



def get_title(volume):
    return volume["volumeInfo"]["title"]



for i in range(0,5):  # author, title, and publishing company.
    print(get_title(book_items_list[i]))
