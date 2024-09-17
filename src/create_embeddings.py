import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

def load_chunks(chunks_dir):
    chunks = []
    for file in sorted(os.listdir(chunks_dir)):
        if file.endswith('.json'):
            with open(os.path.join(chunks_dir, file), 'r') as f:
                chunk_data = json.load(f)
                chunks.append(chunk_data['text'])
    return chunks

def create_embeddings():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chunks_dir = os.path.join(project_root, 'data', 'chunks')
    
    print("Loading chunks...")
    chunks = load_chunks(chunks_dir)
    print(f"Loaded {len(chunks)} chunks")
    
    print("Creating embeddings...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks, show_progress_bar=True)
    
    print("Creating FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    print("Saving FAISS index and chunks...")
    faiss.write_index(index, os.path.join(project_root, 'data', 'faiss_index.bin'))
    np.save(os.path.join(project_root, 'data', 'text_chunks.npy'), chunks)
    
    print("Embeddings created and saved.")

if __name__ == "__main__":
    create_embeddings()