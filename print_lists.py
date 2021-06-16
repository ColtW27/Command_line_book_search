from texttable import Texttable

def print_search_results(search_results):  # prints the search results list
    print()
    print("SEARCH RESULTS")
    print()
    t = Texttable()

    for count, value in enumerate(search_results):
        list_id = count + 1
        title = search_results[value][0]
        authors = search_results[value][1]
        publisher = search_results[value][2]
        t.add_rows([['Id', 'Title', 'Author(s)', 'Publisher'],
                   [list_id, title, authors, publisher]])

    print(t.draw())
    print("\n")


def print_reading_list(reading_list):  # Prints the user's reding list
    t = Texttable()
    print("READING LIST \n")
    for count, value in enumerate(reading_list):
        list_id = count + 1
        title = reading_list[count][0]
        authors = reading_list[count][1]
        publisher = reading_list[count][2]
        t.add_rows([['Id', 'Title', 'Author(s)', 'Publisher'],
                    [list_id, title, authors, publisher]])

    print(t.draw())
    print("\n")
