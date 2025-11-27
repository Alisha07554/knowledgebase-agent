## 🏗️ Architecture Diagram

Below is the end-to-end architecture of the KnowledgeBase Agent:

![Architecture Diagram](assets/architecture.png)

# Overview

KnowledgeBase Agent is an intelligent Retrieval-Augmented Generation (RAG) system that allows users to upload documents and ask questions.
The agent extracts content, stores embeddings, and retrieves the most relevant answers.

# Features

1. Upload PDFs
2. Local Vector DB (Chroma)
3. RAG Retrieval
4. Answers based on your uploaded documents
5. No OpenAI API required
6. Clean UI using Streamlit

# Tech Stack

Python
Streamlit (UI)
LlamaIndex (RAG Engine)
ChromaDB (Vector Storage)
pdfplumber for extraction

# Project Structure
knowledgebase-agent/
│── app.py
│── modules/
│     ├── loader.py
│     ├── embeddings_store.py
│     ├── rag_agent.py
│── docs/ (uploaded documents)
│── chroma_db/ (auto-created)
│── README.md
│── requirements.txt

# How to Run
pip install -r requirements.txt
streamlit run app.py

# Limitations

No advanced LLM reasoning (because project runs offline)
Answers depend entirely on document content
More documents require more processing time
Accuracy depends on text clarity inside PDFs

# Future Improvements

Add citations for each answer
Add multi-file support
Add better UI design
Add more file formats
