from get_book_data import get_publisher, get_authors, get_title
# curates a list of the top 5 search results
def create_search_results(book_items_list, search_results):
    for i in range(0, 5):  # author, title, and publishing company.
        list_id = i + 1
        volume = book_items_list[i]
        title = get_title(volume)
        authors = get_authors(volume)
        publisher = get_publisher(volume)

        volume_information = [title, authors, publisher]
        # add volume to search results
        search_results[list_id] = volume_information
    #   under a key of id , offset from index to prevent a 0 list position


def check_for_search_results(book_search_response):
    results = None
    try:
        results = book_search_response["items"]
    except KeyError:
        results = None
        print("I don't have any results for that search.")
    return results


def check_if_still_searching():
    valid_response = ""

    while valid_response == "":
        valid_response = input(
            """Would you like to try a different search? (Yes/No) \n""").lower()
        if valid_response == "no":
            break
        elif valid_response == "yes":
            break
        else:
            print(
                "Looks like you entered a response other than Yes or No. Please try again.")
            valid_response = ""
    return valid_response
