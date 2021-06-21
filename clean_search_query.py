def clean_search(query):
    query = query.strip()
    query = query.split(" ")
    query = filter(lambda x: x != "", query)
    return "".join(list(query))


# Testcases 
# these can be run in this file to ensure that the smae result is achieved
# The output should all be strings devoid of any whitespace
print(clean_search("Dance!")) # output => "Dance!"
print(clean_search("Dance music"))  # output => "Dancemusic"
print(clean_search(" Dance  !   music"))  # output => "Dance!music"
# output => "Danceonthestreet!"
print(clean_search("    Dance    on   the street!"))
print(clean_search("Dance     !"))  # output => "Dance!"

