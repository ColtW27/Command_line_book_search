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

def get_list_number_for_book_replacement():
    book_to_replace = ""
    while book_to_replace not in range(1, 6):
        try:
            book_to_replace = int(input("""Which book would you like \
to replace? Please select a list number. \n"""))
        except ValueError:
            book_to_replace = ""
            if book_to_replace not in range(1, 6):
                print("That response is not a number between 1 and 5. Please try again.")

    return int(book_to_replace) - 1
    

def get_book_to_add_search_list_number():
    book_to_replace = ""
    while book_to_replace not in range(1, 6):
        try:
            book_to_replace = int(input("""Which book would you like \
to add? Please select a list number. \n"""))
        except ValueError:
            book_to_replace = ""
        if book_to_replace not in range(1, 6):
                print("That response is not a number between 1 and 5. Please try again.")
    return int(book_to_replace)


def check_if_still_searching():
    valid_response = ""

    while valid_response == "":
        valid_response = input("""Would you like to try a different search? (Yes/No) """).lower()
        if valid_response == "no":
            break
        elif valid_response == "yes":
            break
        else:
            print("Looks like you entered a response other than Yes or No. Please try again.")
            valid_response = ""
    return valid_response

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

                book_to_replace = get_list_number_for_book_replacement()
                reading_list[book_to_replace] = volume_from_search_results
            elif replace_item == "no":
                break
            else:
                print("""Sorry, you seem to have entered an invalid response, \
please reread the prompt for clarification and try again.""")

    print_search_results(search_results)
    print_reading_list(reading_list)

      
still_searching = "yes"


while still_searching == "yes":  # runs the full query cycle
    get_search_queury()
    create_search_results()  # curates a list of the top 5 search results
    print_search_results(search_results)  # prints the search results list
    print_reading_list(reading_list)  # prints the reading list

    add_to_reading_list = input(f"""Would you like to add any of these to your \
    reading list?  (Yes/no)""").lower()

    while add_to_reading_list == "yes":
        book_to_add = get_book_to_add_search_list_number()

        add_book_to_reading_list(book_to_add)

        add_to_reading_list = input("""I've added that book for you, would you \
like to add another? (Yes/No) \n""")

    still_searching = check_if_still_searching()
    # still_searching = input("""Would you like to try a different search? (Yes/No) \
    #     """).lower()
    
print("Thanks for visiting!")
