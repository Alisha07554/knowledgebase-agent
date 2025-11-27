##  Architecture Diagram
                 ┌──────────────────────┐
                 │      User Uploads     │
                 │        PDFs            │
                 └──────────┬────────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Document Loader     │
                 │ (extract text from    │
                 │     PDF files)        │
                 └──────────┬────────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     Chunking Module   │
                 │ (split text into      │
                 │  small chunks)        │
                 └──────────┬────────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Vector Embeddings    │
                 │ (convert chunks into  │
                 │    numerical vectors) │
                 └──────────┬────────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   ChromaDB Storage    │
                 │ (store vectors for    │
                 │    fast retrieval)     │
                 └──────────┬────────────┘
                            │
                            ▼
                 ┌────────────────────────┐
                 │       User Query        │
                 │ (asks a question in UI) │
                 └──────────┬──────────────┘
                            │
                            ▼
                 ┌────────────────────────┐
                 │    Vector Retrieval     │
                 │ (find similar chunks    │
                 │     from ChromaDB)      │
                 └──────────┬──────────────┘
                            │
                            ▼
                 ┌────────────────────────┐
                 │     Local LLM (free)    │
                 │ (generate final answer   │
                 │   using retrieved data)  │
                 └──────────┬──────────────┘
                            │
                            ▼
                 ┌────────────────────────┐
                 │      Final Answer       │
                 │  Returned to the User   │
                 └────────────────────────┘

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
1.Python

2.Streamlit (UI)

3.LlamaIndex (RAG Engine)

4.ChromaDB (Vector Storage)

5.pdfplumber for extraction

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
1. pip install -r requirements.txt
2. streamlit run app.py

# Limitations
1.No advanced LLM reasoning (because project runs offline)   

2.Answers depend entirely on document content

3.More documents require more processing time

4.Accuracy depends on text clarity inside PDFs

# Future Improvements
1.Add citations for each answer

2.Add multi-file support

3.Add better UI design

4.Add more file formats
