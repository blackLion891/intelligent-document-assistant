from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
def get_embedding_model():
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs = {
            "device" : "cpu",
            "token": os.getenv("HF_TOKEN")
        },
        encode_kwargs = {
            "normalize_embeddings" : True
        }
    )
    return embeddings


def generate_embeddings(chunks):
    embedding_model = get_embedding_model()

    texts = [
        chunk.page_content
        for chunk in chunks
    ]

    vectors = embedding_model.embed_documents(texts)

    return vectors