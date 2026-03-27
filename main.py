import os
import json
import time


import json
import os

from src.retrieval.chunking import chunk_transcript
from src.retrieval.embeddings import get_embeddings
from src.retrieval.vector_store import create_vector_store

from src.ingestion.vtt_parser import parse_vtt_to_json
from src.ingestion.cleaner import clean_transcript
from src.ingestion.transcript_loader import fetch_and_save_transcript
from src.qa.evaluate import load_golden_dataset, evaluate_rag
from src.qa.rag_pipeline import run_rag
from src.qa.generate_qa import generate_qa_from_chunks, save_qa_pairs

# VIDEO_URLS = [
#     # "https://www.youtube.com/watch?v=aircAruvnKk",
#     # "https://www.youtube.com/watch?v=wjZofJX0v4M",
#     "https://www.youtube.com/watch?v=fHF22Wxuyw4",
#     # "https://www.youtube.com/watch?v=C6YtPJxNULA",
# ]

# for url in VIDEO_URLS:
#     fetch_and_save_transcript(url)
#     time.sleep(15)   # 🔥 increase delay


# def process_vtt_files(raw_dir="data/raw", processed_dir="data/processed"):
#     os.makedirs(processed_dir, exist_ok=True)

#     for file in os.listdir(raw_dir):
#         if file.endswith(".vtt"):
#             file_path = os.path.join(raw_dir, file)

#             # 🔥 Parse
#             parsed = parse_vtt_to_json(file_path)

#             # 🧹 Clean
#             cleaned = clean_transcript(parsed)

#             # 💾 Save
#             output_path = os.path.join(processed_dir, file.replace(".vtt", ".json"))

#             with open(output_path, "w", encoding="utf-8") as f:
#                 json.dump(cleaned, f, indent=4)

#             print(f"✅ Processed: {output_path}")


# process_vtt_files()



def load_processed_data(folder="data/processed"):
    all_chunks = []

    for file in os.listdir(folder):
        if file.endswith(".json"):
            path = os.path.join(folder, file)

            with open(path, "r", encoding="utf-8") as f:
                transcript = json.load(f)

            chunks = chunk_transcript(transcript)

            # add video id
            for c in chunks:
                c["video"] = file

            all_chunks.extend(chunks)

    return all_chunks


# 🔥 LOAD DATA
chunks = load_processed_data()

# 🔥 EMBEDDINGS
embeddings = get_embeddings()

# 🔥 VECTOR DB
vector_store = create_vector_store(chunks, embeddings)

from src.qa.rag_pipeline import run_rag
from src.qa.grok_client import query_grok

# test query
query = "Explain backpropagation in neural networks"

answer, docs = run_rag(query, vector_store, query_grok)

print("\n🧠 Answer:\n", answer)

print("\n📍 Sources:")
for doc in docs:
    print(doc.metadata)
    
    

qa_pairs = generate_qa_from_chunks(chunks, limit=5)
save_qa_pairs(qa_pairs)



qa_pairs = load_golden_dataset()

results = evaluate_rag(vector_store, run_rag, qa_pairs)