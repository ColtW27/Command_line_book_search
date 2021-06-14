import json  # built in module for json data
from urllib.request import urlopen  # Python built-in module for opemning and reading URLS


reading_list = []  # Holds the user's reading list, this can only have 5 items
search_results = {}  # create an object to store the seach results so that they
# are accessible to add to reading list by id

def get_search_queury():  # gets query from user and a response back
    api = "https://www.googleapis.com/books/v1/volumes?q=search_query:"
    search_query = input(f"Please enter your search, without spaces. \n ")  # .strip()
    # send a restful request and receives the response as JSON. This is the entire
    response = urlopen(api + search_query)
    # Allows the parsing and conversion of JSON into Python
    # Represents the entire object and data on search
    book_search_response = json.load(response)
    # Items array that holds the volumes (books)
    global book_items_list
    book_items_list = book_search_response["items"]


def get_authors(volume):  # returns the list of authors for the volume 
    if "authors" in volume["volumeInfo"]:
        return volume["volumeInfo"]["authors"]
    else:
        return "Unavailable"


def get_title(volume):  # returns the title for the volume
    if "title" in volume["volumeInfo"]:
        return volume["volumeInfo"]["title"]
    else:
        return "Unavailable"


def get_publisher(volume):  # returns the publisher for the volume
    if "publisher" in volume["volumeInfo"]:
        return volume["volumeInfo"]["publisher"]
    else:
        return "Unavailable"


def create_search_results():  # curates a list of the top 5 search results
    for i in range(0,5):  # author, title, and publishing company.
        list_id = i + 1
        volume = book_items_list[i]
        title = get_title(volume)
        authors = get_authors(volume)
        publisher = get_publisher(volume)

        volume_information = [title, authors, publisher]
        search_results[list_id] = volume_information  # add volume to search results
    #   under a key of id , offset from index to prevent a 0 list position


def print_search_results(search_results):  # prints the search results list
    print("SEARCH RESULTS \n")
    for count, value in enumerate(search_results):
        list_id = count + 1
        volume_information = search_results[value]
        print(f"({list_id})  {volume_information} ")
    print("\n")  


def print_reading_list(reading_list):  # Prints the user's reding list
    print("READING LIST \n")
    for count, value in enumerate(reading_list):
        print(f"({count + 1}) {value}")
    print("\n")


def add_book_to_reading_list(volume):
    volume = int(volume)
    volume_from_search_results = search_results[volume]  # gets the current volume
    if len(reading_list) < 5:
        reading_list.append(volume_from_search_results)
    else:  # at this point the user's reading list is full
        replace_item = "no"
        while replace_item != 'yes':
            replace_item = input("""It looks like your list is full. Would you like \
to replace an item in your list? (Yes/No) \n""")
            if replace_item == "yes":
                print_search_results(search_results)
                print_reading_list(reading_list)

                book_to_replace = int(input("""Okay, which book would you like \
to replace? Please select a list number. \n""")) - 1
                reading_list[book_to_replace] = volume_from_search_results
            elif replace_item == "no":
                break
            else:
                print("""Sorry, you seem to have entered an invalid response, please reread the prompt for clarification and try again.""")
    print_search_results(search_results)
    print_reading_list(reading_list)
# def add_book_to_reading_list(volume):
#     volume = int(volume)
#     volume_from_search_results = search_results[volume]  # gets the current volume
#     if len(reading_list) < 5:
#         reading_list.append(volume_from_search_results)
#     else:  # at this point the user's reading list is full
#         replace_item = input("""It looks like your list is full. Would you like \
# to replace an item in your list? (Yes/No) \n""")
#         if replace_item == "yes":
#             print_search_results(search_results)
#             print_reading_list(reading_list)

#             book_to_replace = int(input("""Okay, which book would you like \
# to replace? Please select a list number. \n""")) - 1
#             reading_list[book_to_replace] = volume_from_search_results

#     print_search_results(search_results)
#     print_reading_list(reading_list)

      
still_searching = "yes"


while still_searching == "yes":  # runs the full query cycle
    get_search_queury()
    create_search_results()  # curates a list of the top 5 search results
    print_search_results(search_results)  # prints the search results list
    print_reading_list(reading_list)  # prints the reading list

    add_to_reading_list = input(f"""Would you like to add any of these to your \
    reading list?  (Yes/no)""").lower()

    while add_to_reading_list == "yes":
        book_to_add = input(
            f"""Okay, which book would you like to add to your reading list? \
    Please specify a list number. \n""")

        add_book_to_reading_list(book_to_add)

        add_to_reading_list = input("""I've added that book for you, would you \
like to add another? (Yes/No) \n""")

    still_searching = input("""Would you like to try a different search? (Yes/No) \
        """).lower()
    
print("Thanks for visiting!")
