def build_prompt(query, docs):
    context = ""

    for i, doc in enumerate(docs):
        context += f"\n[Chunk {i+1}]\n{doc.page_content}\n"

    prompt = f"""
You are an AI assistant answering based ONLY on the provided context.

Context:
{context}

Question:
{query}

Instructions:
- Answer clearly
- Use only the context
- If not found, say "Not found in context"

Answer:
"""
    return prompt


def run_rag(query, vector_store, grok_client):
    docs = vector_store.similarity_search(query, k=3)

    prompt = build_prompt(query, docs)

    answer = grok_client(prompt)

    return answer, docs