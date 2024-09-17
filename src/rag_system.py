import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RAGSystem:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.text_chunks = np.load(os.path.join(project_root, 'data', 'text_chunks.npy'), allow_pickle=True)
        print(f"Loaded {len(self.text_chunks)} text chunks")
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.text_chunks)
        print("TF-IDF vectorizer and matrix created")

    def retrieve(self, query, k=3):
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)[0]
        top_k_indices = similarities.argsort()[-k:][::-1]
        retrieved_chunks = [self.text_chunks[i] for i in top_k_indices]
        print(f"Retrieved {len(retrieved_chunks)} chunks for query: {query}")
        return retrieved_chunks

    def generate(self, query, retrieved_chunks):
        context = " ".join(retrieved_chunks)
        print(f"Context length: {len(context)} characters")
        
        query_words = set(query.lower().split())
        sentences = context.split('.')
        relevant_sentences = []
        
        for sent in sentences:
            sent = sent.strip()
            if sent and any(word in sent.lower() for word in query_words):
                relevant_sentences.append(sent)

        if relevant_sentences:
            answer = '. '.join(relevant_sentences[:3])  # Return up to 3 relevant sentences
            print(f"Found {len(relevant_sentences)} relevant sentences")
            return f"Based on the retrieved information: {answer}"
        else:
            print("No relevant sentences found")
            return "I couldn't find a specific answer to that question in the given context. The topic you're asking about might not be covered in the available text."

    def query(self, user_query):
        retrieved_chunks = self.retrieve(user_query)
        response = self.generate(user_query, retrieved_chunks)
        return response