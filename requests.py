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


def get_authors(volume):
    return volume["volumeInfo"]["authors"]

def get_title(volume):
    return volume["volumeInfo"]["title"]

def get_publisher(volume):
    if "publisher" in volume["volumeInfo"]:
        return volume["volumeInfo"]["publisher"]
    else:
        return "Unavailable"

search_results = {}  # create an object to store the seach results so that they 
# are accessible to add to reading list by id

def create_search_results():
    for i in range(0,5):  # author, title, and publishing company.
        list_id = i + 1
        volume = book_items_list[i]
        title = get_title(volume)
        authors = get_authors(volume)
        publisher = get_publisher(volume)

        volume_information = [title, authors, publisher]
        search_results[list_id] = volume_information  # add volume to search results
    #   under a key of id , offset from index to prevent a 0 list position
        # print(f"({list_id})  {volume_information}")


def print_search_results(search_results):
    print("SEARCH RESULTS \n")
    for count, value in enumerate(search_results):
        list_id = count - 1
        volume_information = search_results[value]
        # print(f"search_results[value]")
        print(f"({list_id})  {volume_information} ")
    print("\n")  

create_search_results()
print_search_results(search_results)

add_to_reading_list = input(f"""Would you like to add any of these to your \
reading list?  (Yes/no)""").lower()

def print_reading_list(reading_list):
    print("READING LIST \n")
    for count, value in enumerate(reading_list):
        print(f"{count + 1} {value}")
    print("\n")

reading_list = []  # this can only have 5 items


def add_book_to_reading_list(volume):
    volume = int(volume)
    volume_from_search_results = search_results[volume]
    if len(reading_list) < 5:
        reading_list.append(volume_from_search_results)
    else:
        replace_item = input("""It looks like your list is full. Would you like \
to replace an item in your list? (Yes/No) \n""")
        if replace_item == "yes":
            # print(reading_list)
            print_search_results(search_results)
            print_reading_list(reading_list)

            book_to_replace = int(input("""Okay, which book would you like \
to replace? Please select a list number. \n""")) - 1
            reading_list[book_to_replace] = volume_from_search_results
    # print(reading_list)
    print_search_results(search_results)
    print_reading_list(reading_list)

while add_to_reading_list == "yes":
    book_to_add = input(
        f"""Okay, which book would you like to add to your reading list? \
Please specify a list number. \n""")
    add_book_to_reading_list(book_to_add)

    add_to_reading_list = input("""I've added that book for you, would you like to \
add another? (Yes/No) \n""")


print("Thanks for visiting!")
        

