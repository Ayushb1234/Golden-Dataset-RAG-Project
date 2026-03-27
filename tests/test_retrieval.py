query = "How does backpropagation work?"

docs = vector_store.similarity_search(query, k=3)

for i, doc in enumerate(docs):
    print(f"\nResult {i+1}:")
    print(doc.page_content)
    print(doc.metadata)