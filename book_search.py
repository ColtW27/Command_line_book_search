from texttable import Texttable  # module for creating tables with the information
import json  # built in module for json data
from urllib.request import urlopen  # Python built-in module for opemning and reading URLS
from intro import intro
from get_book_data import get_publisher, get_authors, get_title, get_book_to_add_search_list_number, get_list_number_for_book_replacement
from add_volumes import add_book_to_reading_list
from print_lists import print_reading_list, print_search_results
from search_results import create_search_results
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
        print("\n")
        search_query = input(f"Please enter your search, without spaces. \n")  # .strip()
        # send a restful request and receives the response as JSON. This is the entire
        response = urlopen(api + search_query)
        # Allows the parsing and conversion of JSON into Python
        # Represents the entire object and data on search
        book_search_response = json.load(response)
        # Items array that holds the volumes (books)
        book_items_list = check_for_search_results(book_search_response)


# def create_search_results(book_items_list, search_results):  # curates a list of the top 5 search results
#     for i in range(0,5):  # author, title, and publishing company.
#         list_id = i + 1
#         volume = book_items_list[i]
#         title = get_title(volume)
#         authors = get_authors(volume)
#         publisher = get_publisher(volume)

#         volume_information = [title, authors, publisher]
#         search_results[list_id] = volume_information  # add volume to search results
#     #   under a key of id , offset from index to prevent a 0 list position


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


def begin_search():
    get_search_query()  # gets query from user and response from the books api
    # curates a list of the top 5 search results
    create_search_results(book_items_list, search_results)
    print_search_results(search_results)  # prints the search results list
    print_reading_list(reading_list)  # prints the reading list

    add_to_reading_list = add_another_book_validation("first_add")  # validates yes or no response

    while add_to_reading_list == "yes":
        book_to_add = get_book_to_add_search_list_number()  # gets the number 
# and handles errors for adding books

        add_book_to_reading_list(book_to_add, search_results, reading_list)  # Takes book and appends or 
#replaces items to reading list as needed

        add_to_reading_list = add_another_book_validation("subsequent_add")  # validates yes or no response


def run_search():  # runs the program
    still_searching = "yes"
    print("\n")
    intro()
    print("""Hello! Welcome to the Google Books Command Line Search Tool! \n
I look forward to helping you create a list of your next great reads! \n """)

    while still_searching == "yes":  # runs the full query cycle
        begin_search()
        still_searching = check_if_still_searching()  # handles errors and logic to
    # continue or end book search 
    print("Thanks for visiting!") # being friendly is helpful


run_search()
