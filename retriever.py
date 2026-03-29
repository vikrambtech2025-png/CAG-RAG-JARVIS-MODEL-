from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = open("data/docs.txt").read().split("\n")

embeddings = model.encode(documents)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def retrieve(query, k=2):
    q_embedding = model.encode([query])
    distances, indices = index.search(np.array(q_embedding), k)
    
    results = [documents[i] for i in indices[0]]
    return results