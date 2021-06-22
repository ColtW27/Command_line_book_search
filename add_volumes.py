from print_lists import print_reading_list, print_search_results
from get_book_data import get_list_number_for_book_replacement


def replace_book(volume_id, search_results, reading_list):
    volume_from_search_results = search_results[volume_id]

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
            statement = "I've added that book for you."
            return statement
        elif replace_item == "no":
            statement = "Okay, I'll leave your reading list as it was for now. "
            replace_item == "yes"
            return statement
        else:
            print("""Sorry, you seem to have entered an invalid response, \
please reread the prompt for clarification and try again.""")


def add_book_to_reading_list(volume_id, search_results,reading_list):
    volume_id = int(volume_id) # gets the current volume_id id
    volume_from_search_results = search_results[volume_id] 
    statement = ""

    if len(reading_list) < 5:
        reading_list.append(volume_from_search_results)  # adds book to read list
    else:  # at this point the user's reading list is full
        statement = replace_book(volume_id, search_results, reading_list)   
# replace_book abstracts whether or not to replace book and returns statement
# returned statement depends on whenther book is replaced
    print_search_results(search_results)
    print_reading_list(reading_list)
    print(statement)


def add_another_book_validation(key):
    reponse_key = {"first_add": """Would you like to add any of these to your \
reading list?  (Yes/no) \n""", "subsequent_add": """Would you \
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
