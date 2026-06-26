documents = [
    "Maintenance manual for Pump A",
    "Safety SOP for Boiler",
    "Inspection report of Generator",
    "Compliance checklist for Industry"
]

def search_database(query):
    for doc in documents:
        if query.lower() in doc.lower():
            return doc

    return "No matching document found."
