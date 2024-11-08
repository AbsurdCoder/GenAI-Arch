"""
# Step 1: Create and index document embeddings using FAISS
# Step 2: Querying and retrieving relevant documents using FAISS
# Step 3: Pass the retrieved documents to a generative model (e.g., GPT-3)
"""

import faiss
import numpy as np
# import openai  # Example for GPT-3 or GPT-4 API
import ollama

class RAGPipeline:
    def __init__(self, embeddings):
        print('Initializing the class with embeddings')
        self.document_embeddings = np.stack(embeddings)
        self.document_embeddings = np.squeeze(self.document_embeddings)
        print(f"Embeddings shape: {self.document_embeddings.shape}")

    def index_with_faiss(self):
        # Index embeddings with FAISS
        embedding_dimension = self.document_embeddings.shape[1]
        print(embedding_dimension)
        self.index = faiss.IndexFlatL2(embedding_dimension)
        self.index.add(self.document_embeddings)

    def similarity(self, query_embedding, documents):
        # Perform similarity search in FAISS | Needs query embedding
        k = 2  # Number of nearest neighbors to retrieve
        query_embedding_temp = np.stack(query_embedding)
        query_embedding = np.squeeze(query_embedding_temp)
        print(f"Embeddings shape: {query_embedding.shape}")
        distances, indices = self.index.search(query_embedding, k)

        # Get the most relevant documents based on the nearest neighbors
        retrieved_documents = [documents[i] for i in indices[0]]

        retrieved_context = " ".join(retrieved_documents)  # Combine retrieved documents into context
        return retrieved_context

    def generate_response(self, query, retrieved_context):
        # # Use the retrieved context to generate an answer
        # response = openai.Completion.create(
        #     engine="text-davinci-003",  # or any other GPT-3/4 engine
        #     prompt=f"Answer the question: {query}\nContext: {retrieved_context}",
        #     max_tokens=100
        # )
        prompt = f"Answer the question: {query}\nContext: {retrieved_context}"
        msg = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        # Use the Ollama model to generate a response
        response = ollama.chat(model="llama3.1", messages=msg)
        print(response)
        # Extract and return the generated response
        if response:
            return response['message']['content']
        else:
            return "Sorry, I couldn't generate a response."
