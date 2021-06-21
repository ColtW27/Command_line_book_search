


def clean_search(query):
    query = query.strip()
    query = query.split(" ")
    query = filter(lambda x: x != "", query)
    return "".join(list(query))



