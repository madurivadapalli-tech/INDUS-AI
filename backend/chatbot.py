from rag import retrieve_document

def get_answer(query):
    context = retrieve_document(query)

    return f"""
Question: {query}

Relevant Information:
{context}

AI Response:
This is a sample AI-generated response based on the retrieved industrial document.
"""
