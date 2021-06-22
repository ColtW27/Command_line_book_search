#!/usr/bin/python
# -*- coding: utf-8 -*-
import emoji


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
# This includes quotes, whose inclusion seems to give different search results



