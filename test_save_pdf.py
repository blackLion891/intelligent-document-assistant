
from pathlib import Path

from src.pdf_loader import load_pdf
from src.pdf_repository import save_pdf_details


pdf_path = r"data\PYTHON PROGRAMMING NOTES.pdf"

# Step 2: Load PDF
documents = load_pdf(pdf_path)

print("PDF loaded successfully!")
print("Total pages:", len(documents))

# Step 3: Get PDF information
file_path = Path(pdf_path).resolve()

filename = file_path.name
total_pages = len(documents)

# Step 4: Save PDF details in MySQL
document_id = save_pdf_details(
    filename=filename,
    file_path=str(file_path),
    total_pages=total_pages
)

# Step 5: Display saved information
print("\n========== SAVED PDF DETAILS ==========")

print("Document ID:", document_id)
print("Filename:", filename)
print("File Path:", file_path)
print("Total Pages:", total_pages)

print("\nPDF database testing completed!")
