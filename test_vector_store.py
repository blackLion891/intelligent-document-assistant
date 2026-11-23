from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store

# Step 1: Load PDF
pdf_path = r"data\PYTHON PROGRAMMING NOTES.pdf"

documents = load_pdf(pdf_path)

print("PDF loaded successfully!")
print("Total pages:", len(documents))


# Step 2: Split PDF text
chunks = split_documents(documents)

print("\nText splitting completed!")
print("Total chunks:", len(chunks))

# Step 3: Create ChromaDB vector store
vector_store = create_vector_store(chunks)
print("\nChromaDB vector store created successfully!")
# Step 4: Check stored document count

collection = vector_store._collection

print("Total stored documents:", collection.count())


# Step 5: Test similarity search
query = "What is the main topic of this PDF?"

result = vector_store.similarity_search(
    query,
    k=3
)

# Step 6: Display retrieved chunks
print("\n========== SIMILARITY SEARCH RESULTS ==========")

for index, document in enumerate(result, start=1):
    print(f"\n----- RESULT {index} -----")

    print("Metadata:", document.metadata)

    print("Content:")

    print(document.page_content)

print("\nChromaDB testing completed successfully!")
