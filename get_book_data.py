def list_authors_in_string(authors):
    pass

def get_authors(volume):  # returns the list of authors for the volume
    if "authors" in volume["volumeInfo"]:
        # return volume["volumeInfo"]["authors"]
        authors = list_authors_in_string(volume["volumeInfo"]["authors"])
        return authors
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

#  note for future optimazation, dry up code by combining these two functions, as they are all but identical except for the "- 1"
def get_list_number_for_book_replacement():
    book_to_replace = ""
    while book_to_replace not in range(1, 6):
        try:
            book_to_replace = int(input("""Which book would you like \
to replace? Please select a list number. \n"""))
        except ValueError:  # handles non number inputs
            book_to_replace = ""
        if book_to_replace not in range(1, 6):  # specifies if the input is out of the list range
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
        # specifies if the input is out of the list range
        if book_to_add not in range(1, 6):
            print("That response is not a number between 1 and 5. Please try again.")
    return int(book_to_add)
