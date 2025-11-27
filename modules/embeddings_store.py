import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(text_chunks, persist_dir):
    client = chromadb.PersistentClient(path=persist_dir)
    collection = client.get_or_create_collection(
        name="knowledge_base",
        metadata={"hnsw:space": "cosine"}
    )

    embeddings = model.encode(text_chunks).tolist()
    ids = [f"chunk_{i}" for i in range(len(text_chunks))]
    
    collection.add(ids=ids, embeddings=embeddings, documents=text_chunks)

def load_index(persist_dir):
    client = chromadb.PersistentClient(path=persist_dir)
    return client.get_collection("knowledge_base")
