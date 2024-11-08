import faiss
import numpy as np

# Create a FAISS index
embedding_dimension = 512  # Adjust based on the model's embedding dimension
index = faiss.IndexFlatL2(embedding_dimension)

# Add embeddings to the FAISS index (assuming embeddings are numpy arrays)
index.add(np.array([embedding]))  # Add the generated embedding

# Query to retrieve similar embeddings
query_embedding = np.random.rand(1, embedding_dimension).astype(np.float32)  # Replace with actual query embedding
k = 1  # Number of nearest neighbors
distances, indices = index.search(query_embedding, k)

# Retrieve the most similar embedding and create a prompt
retrieved_embedding = np.array([embedding])[indices[0][0]]


prompt_template = f"""
We retrieved the following relevant embedding for a query:

{', '.join(map(str, retrieved_embedding))}

Using this context, generate an insightful response to the query.
"""

# Send the prompt with embedding to Ollama
response = ollama.create(model="llama3.1", input=prompt_template)
print("Response:", response)