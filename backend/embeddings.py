from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """
    return model.encode(chunks)


def get_query_embedding(query):
    """
    Generate embedding for a user's question.
    """
    return model.encode(query)