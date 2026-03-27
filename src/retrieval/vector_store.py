from langchain.vectorstores import FAISS

def create_vector_store(chunks, embeddings):
    texts = [chunk["text"] for chunk in chunks]
    metadatas = [
        {
            "start": chunk["start"],
            "end": chunk["end"]
        }
        for chunk in chunks
    ]

    vector_store = FAISS.from_texts(texts, embeddings, metadatas=metadatas)

    return vector_store