import ollama



class ollama_helpers:
    def __init__(self):
        self.model_name="llama3.1"
        print(f"Init {self.model_name}")


    def embedding(self, text):
        embedding_response = ollama.embed(model=self.model_name, input=text)

        # Extract the embeddings
        embedding = embedding_response['embeddings']

        # Print the embedding (can be a vector)
        return embedding


