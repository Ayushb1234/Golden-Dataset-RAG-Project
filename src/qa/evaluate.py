import json


def load_golden_dataset(path="golden_dataset/qa_pairs.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def evaluate_rag(vector_store, rag_pipeline, qa_pairs):
    results = []

    correct = 0

    for i, qa in enumerate(qa_pairs):
        question = qa["question"]
        expected_source = qa["source"]

        answer, docs = rag_pipeline(question, vector_store)

        # 🔍 check top retrieved doc
        retrieved_source = docs[0].metadata.get("video", "unknown")

        is_correct = expected_source.split("|")[0] in retrieved_source

        if is_correct:
            correct += 1

        results.append({
            "question": question,
            "expected": expected_source,
            "retrieved": retrieved_source,
            "correct": is_correct
        })

        print(f"\nQ{i+1}: {question}")
        print(f"Expected: {expected_source}")
        print(f"Retrieved: {retrieved_source}")
        print(f"✅ Correct" if is_correct else "❌ Wrong")

    accuracy = correct / len(qa_pairs)

    print("\n📊 Accuracy:", accuracy)

    return results