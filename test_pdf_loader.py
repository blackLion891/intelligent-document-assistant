from src.pdf_loader import load_pdf

pdf_path = r"data\PYTHON PROGRAMMING NOTES.pdf"

documents = load_pdf(pdf_path)
print("PDF loaded successfully!")
print("Total pages:", len(documents))
for index, document in enumerate(documents,start=1):
    print(f"\n========== PAGE {index} ==========")
    print("Metadata:", document.metadata)
    print("Extracted Text:")
    print(document.page_content)