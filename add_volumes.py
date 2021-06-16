from print_lists import print_reading_list, print_search_results

def add_book_to_reading_list(volume, search_results,reading_list):
    volume = int(volume)
    # gets the current volume
    volume_from_search_results = search_results[volume]
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
                print_search_results(search_results)
                print_reading_list(reading_list)
                print("Okay, I'll leave your reading list as it was for now. ")
                replace_item == "yes"
                break
            else:
                print("""Sorry, you seem to have entered an invalid response, \
please reread the prompt for clarification and try again.""")

    print_search_results(search_results)
    print_reading_list(reading_list)