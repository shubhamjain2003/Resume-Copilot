import chromadb

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="chroma_db")

# Create (or load) the collection
collection = client.get_or_create_collection(
    name="resume"
)


def store_sections(sections, embeddings):
    """
    Store resume sections and their embeddings in ChromaDB.
    """

    # Delete existing documents (if any)
    try:
        existing = collection.get()

        if existing["ids"]:
            collection.delete(ids=existing["ids"])

    except Exception:
        pass

    ids = []
    documents = []
    metadatas = []
    vectors = []

    for idx, ((title, content), embedding) in enumerate(
        zip(sections.items(), embeddings)
    ):

        ids.append(str(idx))

        documents.append(content)

        metadatas.append(
            {
                "section": title
            }
        )

        vectors.append(embedding.tolist())

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=vectors,
        metadatas=metadatas
    )


def search_sections(query_embedding, top_k=3):
    """
    Search the most relevant resume sections using vector similarity.
    """

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results


def get_section(section_name):
    """
    Retrieve a specific resume section using metadata.
    """

    results = collection.get(
        where={"section": section_name}
    )

    if results["documents"]:
        return results["documents"][0]

    return None


def print_all_sections():
    """
    Debug function to print all stored sections.
    """

    results = collection.get()

    print("\n========== STORED SECTIONS ==========\n")

    for metadata, document in zip(results["metadatas"], results["documents"]):
        print(f"Section: {metadata['section']}")
        print("-" * 60)
        print(document[:300])
        print()