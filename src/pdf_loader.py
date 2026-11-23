from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path:str):
    file_path = Path(pdf_path)

    if not file_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    loader = PyPDFLoader(str(file_path))

    documents = loader.load()

    return documents