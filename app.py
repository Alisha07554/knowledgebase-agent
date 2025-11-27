import streamlit as st
import os
from modules.loader import load_documents_from_folder
from modules.embeddings_store import build_index, load_index
from modules.rag_agent import answer_query

DOCS_DIR = "docs"
DB_DIR = "chromadb_store"

st.title("Local KnowledgeBase (No API Needed)")

uploaded = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if uploaded:
    for file in uploaded:
        with open(os.path.join(DOCS_DIR, file.name), "wb") as f:
            f.write(file.getbuffer())
    st.success("Uploaded!")

if st.button("Build Index"):
    docs = load_documents_from_folder(DOCS_DIR)

    chunks = []
    for d in docs:
        while len(d) > 700:
            chunks.append(d[:700])
            d = d[700:]
        chunks.append(d)

    build_index(chunks, DB_DIR)
    st.success("Index Built Successfully!")

if st.button("Load Index"):
    collection = load_index(DB_DIR)
    st.success("Index Loaded!")

query = st.text_input("Ask a question")

if st.button("Get Answer"):
    collection = load_index(DB_DIR)
    answer = answer_query(collection, query)
    st.write(answer)
