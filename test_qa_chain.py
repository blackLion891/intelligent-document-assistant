from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.qa_chain import answer_question


# Step 1: Load PDF
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

print("\nChromaDB vector store created successfully!")

# Step 4: Ask a question
question = input("\nEnter your question about the PDF: ")


# Step 5: Generate answer using Groq

print("\nGenerating answer...\n")
answer = answer_question(
    vector_store,
    question
)

# Step 6: Display answer
print("========== CHATBOT ANSWER ==========")
print(answer)

print("\nQuestion-answering test completed!")