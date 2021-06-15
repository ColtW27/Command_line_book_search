from texttable import Texttable
import json  # built in module for json data
from urllib.request import urlopen  # Python built-in module for opemning and reading URLS


reading_list = []  # Holds the user's reading list, this can only have 5 items
search_results = {}  # create an object to store the seach results so that they
# are accessible to add to reading list by id


def check_for_search_results(book_search_response):
    results = None
    try:
        results = book_search_response["items"]
    except KeyError:
        results = None
        print("I don't have any results for that search.")
    return results


def get_search_query():  # gets query from user and a response back
    global book_items_list 
    book_items_list = None
    while book_items_list == None:
        api = "https://www.googleapis.com/books/v1/volumes?q=search_query:"
        search_query = input(f"Please enter your search, without spaces. \n")  # .strip()
        # send a restful request and receives the response as JSON. This is the entire
        response = urlopen(api + search_query)
        # Allows the parsing and conversion of JSON into Python
        # Represents the entire object and data on search
        book_search_response = json.load(response)
        # Items array that holds the volumes (books)
        book_items_list = check_for_search_results(book_search_response)


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
    print()
    t = Texttable()
    for count, value in enumerate(search_results):
        list_id = count + 1
        volume_information = search_results[value]
        title = search_results[value][0]
        authors = search_results[value][1]
        publisher = search_results[value][2]
        # title = volume_information["title"]
        # print(f"({list_id}) {title}, {authors}, {publisher} ")
        t.add_rows([['Id','Title', 'Author(s)', 'Publisher'], [list_id, title, authors, publisher]])
        # t.add_rows([['Title', 'Author(s)', 'Publisher'], ['The Lust for Blood', [
        #     'Jeffrey A. Kottler', 'jebidiah roosy'], " Prometheus Books"], ['Vehicles ABC', ['Nosy Crow'], "Nosy Crow"]])
    print(t.draw())
    print("\n")  



    
# def print_search_results(search_results):  # prints the search results list
#     print("SEARCH RESULTS \n")
#     for count, value in enumerate(search_results):
#         list_id = count + 1
#         volume_information = search_results[value]
#         print(f"({list_id})  {volume_information} ")
#     print("\n")  


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
    book_to_add = ""
    while book_to_add not in range(1, 6):
        try:
            book_to_add = int(input("""Which book would you like \
to add? Please select a list number. \n"""))
        except ValueError:
            book_to_add = ""
        if book_to_add not in range(1, 6):
                print("That response is not a number between 1 and 5. Please try again.")
    return int(book_to_add)


def add_another_book_validation(key):
    reponse_key = {"first_add": """Would you like to add any of these to your \
reading list?  (Yes/no) \n""", "subsequent_add": """I've added that book for you, would you \
like to add another? (Yes/No) \n"""}

    valid_response = ""

    while valid_response == "":
        valid_response = input(reponse_key[key]).lower()
        if valid_response == "no":
            break
        elif valid_response == "yes":
            break
        else:
            print("""Looks like you entered a response other than Yes or No. \
Please try again.""")
            valid_response = ""
    return valid_response

def check_if_still_searching():
    valid_response = ""

    while valid_response == "":
        valid_response = input("""Would you like to try a different search? (Yes/No) \n""").lower()
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

                book_to_replace = get_list_number_for_book_replacement()  # Abstracts
# error handling and gets the proper index for the replacement book
                reading_list[book_to_replace] = volume_from_search_results
            elif replace_item == "no":
                break
            else:
                print("""Sorry, you seem to have entered an invalid response, \
please reread the prompt for clarification and try again.""")

    print_search_results(search_results)
    print_reading_list(reading_list)

      
still_searching = "yes"


def intro():
    print(""" 
░█▀▄░█▀█░█▀█░█░█        
░█▀▄░█░█░█░█░█▀▄        
░▀▀░░▀▀▀░▀▀▀░▀░▀        
░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█░█
░▀▀█░█▀▀░█▀█░█▀▄░█░░░█▀█
░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀                                                                        
    """)

def begin_search():
    # print("\n")
#     intro()
#     print("""Hello! Welcome to the Google Books Command Line Search Tool! \n
# I look forward to helping you create a list of your next great reads! \n """)
    get_search_query()
    create_search_results()  # curates a list of the top 5 search results
    print_search_results(search_results)  # prints the search results list
    print_reading_list(reading_list)  # prints the reading list

    add_to_reading_list = add_another_book_validation("first_add")

    while add_to_reading_list == "yes":
        book_to_add = get_book_to_add_search_list_number()  # gets the number 
# and handles errors for adding books

        add_book_to_reading_list(book_to_add)  # Takes book and appends or 
#replaces items to reading list as needed

        add_to_reading_list = add_another_book_validation("subsequent_add")  # validates yes or no


while still_searching == "yes":  # runs the full query cycle
    print("\n")
    intro()
    print("""Hello! Welcome to the Google Books Command Line Search Tool! \n
I look forward to helping you create a list of your next great reads! \n """)
    begin_search()
    still_searching = check_if_still_searching()  # handles errors and logic to
# continue or end book search 
print("Thanks for visiting!") # being friendly is helpful


t = Texttable()
t.add_rows([['Title', 'Author(s)', 'Publisher'], ['The Lust for Blood', [
           'Jeffrey A. Kottler'], " Prometheus Books"], ['Vehicles ABC', ['Nosy Crow'], "Nosy Crow"]])
print(t.draw())
