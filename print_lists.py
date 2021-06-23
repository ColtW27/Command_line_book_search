from texttable import Texttable

def print_search_results(search_results):  # prints the search results list
    print()
    print("SEARCH RESULTS")
    print()
    t = Texttable()  # creates a blank texttable 
    for count, value in enumerate(search_results):  # iterates over search results to build out table
        list_id = count + 1  # offset to remove zero index from table 
        title = search_results[value][0]
        authors = search_results[value][1]
        publisher = search_results[value][2]
        t.add_rows([['Id', 'Title', 'Author(s)', 'Publisher'],
                   [list_id, title, authors, publisher]])  # adds data in each row

    print(t.draw())  # draws the table to the console
    print("\n")


def print_reading_list(reading_list):  # Prints the user's reding list
    t = Texttable()  # creats new blank texttable
    print("READING LIST \n")
    # iterates over reading_list to build out table
    for count, value in enumerate(reading_list):
        list_id = count + 1  # offset to remove zero index from table
        title = reading_list[count][0]
        authors = reading_list[count][1]
        publisher = reading_list[count][2]
        t.add_rows([['Id', 'Title', 'Author(s)', 'Publisher'],
                    [list_id, title, authors, publisher]])  # adds data in each row

    print(t.draw())  # draws the table to the console
    print("\n")
