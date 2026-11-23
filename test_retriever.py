from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import retrieve_relevant_chunks

pdf_path = r"data\PYTHON PROGRAMMING NOTES.pdf"

documents = load_pdf(pdf_path)

print("PDF loaded successfully!")
print("Total pages:", len(documents))


# Step 2: Split PDF text
chunks = split_documents(documents)

print("\nText splitting completed!")
print("Total chunks:", len(chunks))


# Step 3: Create vector store
vector_store = create_vector_store(chunks)

print("\nVector store created successfully!")


# Step 4: Ask a question
query = "What is the main topic of this PDF?"


# Step 5: Retrieve relevant chunks
results = retrieve_relevant_chunks(
    vector_store,
    query,
    k=3
)

# step 6: Display results
print("\n========== RETRIEVED CHUNKS ==========")

for index, document in enumerate(results, start=1):

    print(f"\n----- RESULT {index} -----")

    print("Metadata:", document.metadata)

    print("Content:")
    print(document.page_content)


print("\nRetrieval testing completed successfully!")
