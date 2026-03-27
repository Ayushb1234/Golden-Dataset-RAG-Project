import json
import os
from src.qa.grok_client import query_grok


def build_qa_prompt(chunk_text):
    return f"""
Generate ONE high-quality QA pair from this context.

Return STRICT JSON only:

{{
  "question": "...",
  "answer": "..."
}}

Context:
{chunk_text}
"""


def generate_qa_from_chunks(chunks, limit=5):
    qa_pairs = []

    for i, chunk in enumerate(chunks[:limit]):
        prompt = build_qa_prompt(chunk["text"])

        try:
            response = query_grok(prompt)

            qa = json.loads(response)

            qa_pairs.append({
                "question": qa["question"],
                "answer": qa["answer"],
                "source": f"{chunk['video']} | {round(chunk['start'], 2)}"
            })

        except Exception as e:
            print(f"❌ Failed on chunk {i}: {e}")
            print("Response:", response)

    return qa_pairs


def save_qa_pairs(qa_pairs, path="golden_dataset/qa_pairs.json"):
    os.makedirs("golden_dataset", exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(qa_pairs, f, indent=4)

    print("✅ Golden dataset saved!")