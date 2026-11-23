
from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.pdf_repository import save_pdf_details
from src.chunk_repository import save_pdf_chunks


# Step 1: Load PDF
pdf_path = r"data\PYTHON PROGRAMMING NOTES.pdf"

documents = load_pdf(pdf_path)

print("PDF loaded successfully!")
print("Total pages:", len(documents))


# Step 2: Split PDF
chunks = split_documents(documents)

print("\nText splitting completed!")
print("Total chunks:", len(chunks))


# Step 3: Save PDF details
from pathlib import Path

file_path = Path(pdf_path).resolve()

document_id = save_pdf_details(
    filename=file_path.name,
    file_path=str(file_path),
    total_pages=len(documents)
)

print("\nDocument ID:", document_id)


# Step 4: Save PDF chunks
saved_count = save_pdf_chunks(
    document_id=document_id,
    chunks=chunks
)


# Step 5: Display results
print("\n========== DATABASE RESULTS ==========")

print("Document ID:", document_id)
print("Total chunks:", len(chunks))
print("Saved chunks:", saved_count)

print("\nPDF chunk storage completed!")
