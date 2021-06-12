import json  # built in module for json data
from urllib.request import urlopen  # Python built-in module for opemning and reading URLS

# create variable to house the api and search query
api = "https://www.googleapis.com/books/v1/volumes?q=search_query:"
search_queury = input(f"Please enter your search \n ") #.strip()

# send a restful request and receives the response as JSON
response = urlopen(api + search_queury)
# Allows the parsing and conversion of JSON into Python
book_data = json.load(response)

print(response)
print(search_queury)
print(book_data["items"][0]['volumeInfo']["title"])
