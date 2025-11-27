import pdfplumber
import os

def load_documents_from_folder(folder_path):
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            text = ""
            with pdfplumber.open(os.path.join(folder_path, file)) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            docs.append(text)
    return docs
