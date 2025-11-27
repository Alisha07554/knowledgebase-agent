from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def answer_query(collection, query):
    query_emb = model.encode([query]).tolist()[0]
    results = collection.query(query_embeddings=[query_emb], n_results=3)
    
    docs = results["documents"][0]
    combined = "\n\n".join(docs)

    return combined
