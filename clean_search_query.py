#!/usr/bin/python
# -*- coding: utf-8 -*-
import emoji


def validate_search_query():
    valid_query = False

    while not valid_query:
        query = input(f"Please enter your search. Include at least one \
alphanumeric character. \n")
        query = clean_search(query)

        if query != "":
            valid_query = True
        else:
            print("Your query seems to be invalid. Please try again.")
    return query

def remove_emoji(text):  # removes emojis from input, credit in resources for 
# removing emojies
    return emoji.get_emoji_regexp().sub(u'', text)

def clean_search(query):  # Takes in a query to remove all white space
    query = remove_emoji(query)  # helper to remove emojies
    query = query.strip()  # removes outer whitespace
    query = query.split(" ")  # splits into a list to separate out valid words
    query = filter(lambda x: x != "", query)  # filter out space
    query =  "".join(list(query))  # convert back to list from filter and combine
    
    return query  # return the new query

# Special characters are left in, as they are able to be processed by the search

# Testcases 
# these can be run in this file to ensure that the smae result is achieved
# The output should all be strings devoid of any whitespace
# print(clean_search("Dance!")) # output => "Dance!"
# print(clean_search("Dance music"))  # output => "Dancemusic"
# print(clean_search(" Dance  !   music"))  # output => "Dance!music"
# # output => "Danceonthestreet!"
# print(clean_search("    Dance    on   the street!"))
# print(clean_search("Dance     !"))  # output => "Dance!"
# print(clean_search("Dance  ""   !"))  # output => "Dance!"
# print(clean_search("    Dance ''   on   the street!"))
# print(clean_search("    Dance    on   the street!"))  # Danceonthestreet!
# print(clean_search("    Dance    on  😁 the street!")) # Danceonthestreet!
# print(clean_search("    Dance    on   the🚨street!"))  # Danceonthestreet!


