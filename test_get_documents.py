
from src.pdf_repository import get_all_documents


# Step 1: Retrieve all PDF documents
documents = get_all_documents()


# Step 2: Display document information
print("\n========== UPLOADED PDF DOCUMENTS ==========")

if not documents:

    print("No PDF documents found!")

else:

    for document in documents:

        print("\nDocument ID:", document["document_id"])

        print("Filename:", document["filename"])

        print("File Path:", document["file_path"])

        print("Total Pages:", document["total_pages"])

        print("Uploaded At:", document["uploaded_at"])

        print("-----------------------------------")


print("\nPDF document retrieval completed!")
