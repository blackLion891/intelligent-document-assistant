from src.pdf_loader import load_pdf
from src.text_splitter import split_documents

pdf_path = r"data\PYTHON PROGRAMMING NOTES.pdf"

documents = load_pdf(pdf_path)

chunks = split_documents(documents)

print("PDF loaded successfully!")

print("Total pages:", len(documents))

print("Total chunks:", len(chunks))

for index, chunk in enumerate(chunks,start=1):
    print(f"\n========== CHUNK {index} ==========")

    print("Metadata:", chunk.metadata)

    print("Chunk Length:", len(chunk.page_content))

    print("Chunk Content:")

    print(chunk.page_content)

print("\n========== CHUNK VALIDATION ==========")

for index, chunk in enumerate(chunks,start=1):

    chunk_length = len(chunk.page_content)

    print(f"Chunk {index}: {chunk_length} characters")

    assert chunk_length <= 1000, "Chunk size exceeded!"


print("\nAll chunks passed validation!")