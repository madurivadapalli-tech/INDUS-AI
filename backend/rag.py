from database import search_database

def retrieve_document(query):
    result = search_database(query)
    return result
