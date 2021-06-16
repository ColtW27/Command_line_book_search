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
