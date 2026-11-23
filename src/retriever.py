
def retrieve_relevant_chunks(vector_store, query, k=3):

    if not query or not query.strip():
        raise ValueError("Please provide a valid question!")

    results = vector_store.similarity_search(
        query,
        k=k
    )

    return results
