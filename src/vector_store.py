from langchain_chroma import Chroma

from src.embeddings import get_embedding_model

def create_vector_store(chunks):

    if not chunks:
        raise ValueError("No document chunks available!")

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name="personal_pdf_collection"
    )

    return vector_store