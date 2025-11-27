import streamlit as st
import os
from modules.loader import load_and_chunk_documents
from modules.embeddings_store import create_vector_store, load_vector_store
from modules.rag_agent import ask_question
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"
CHROMA_DIR = BASE_DIR / "chromadb_store"

st.set_page_config(page_title="KnowledgeBase Agent (Local RAG)", layout="centered")
st.title("📘 KnowledgeBase Agent — Local RAG (No API)")

# Upload
uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for pdf in uploaded_files:
        save_path = DOCS_DIR / pdf.name
        with open(save_path, "wb") as f:
            f.write(pdf.getbuffer())
    st.success("Files saved to docs/. Click 'Ingest' next.")

# Buttons: Ingest / Load
col1, col2 = st.columns(2)

with col1:
    if st.button("Ingest Documents"):
        if not any(DOCS_DIR.glob("*.pdf")):
            st.error("No PDFs found!")
        else:
            chunks = load_and_chunk_documents(str(DOCS_DIR))
            create_vector_store(chunks, str(CHROMA_DIR))
            st.success("Vector DB created successfully!")

with col2:
    if st.button("Load Existing Vector DB"):
        try:
            collection = load_vector_store(str(CHROMA_DIR))
            st.success("Vector DB loaded!")
        except:
            st.error("No vector DB found. Please ingest first.")

# Ask Question
st.header("Ask a Question")
question = st.text_input("Type your question:")

if st.button("Get Answer"):
    try:
        collection = load_vector_store(str(CHROMA_DIR))
        answer = ask_question(collection, question)
        st.write("### Answer:")
        st.write(answer)
    except:
        st.error("Vector DB not available. Ingest documents first.")
