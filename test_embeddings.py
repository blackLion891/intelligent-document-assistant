
from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.embeddings import get_embedding_model, generate_embeddings


# Step 1: Load PDF
pdf_path = r"data\PYTHON PROGRAMMING NOTES.pdf"

documents = load_pdf(pdf_path)

print("PDF loaded successfully!")
print("Total pages:", len(documents))


# Step 2: Split PDF text
chunks = split_documents(documents)

print("\nText splitting completed!")
print("Total chunks:", len(chunks))


# Step 3: Generate embeddings
vectors = generate_embeddings(chunks)

print("\nEmbeddings generated successfully!")

print("Total embeddings:", len(vectors))


# Step 4: Check embedding dimensions
if vectors:
    print("Embedding dimensions:", len(vectors[0]))

    print("\nFirst embedding (first 10 values):")
    print(vectors[0][:10])


# Step 5: Generate query embedding
embedding_model = get_embedding_model()

query = "What is the main topic of this PDF?"

query_vector = embedding_model.embed_query(query)

print("\nQuery embedding generated successfully!")

print("Query dimensions:", len(query_vector))
