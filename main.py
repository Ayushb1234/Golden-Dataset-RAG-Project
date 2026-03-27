import os
import json
import time

from src.ingestion.vtt_parser import parse_vtt_to_json
from src.ingestion.cleaner import clean_transcript
from src.ingestion.transcript_loader import fetch_and_save_transcript


VIDEO_URLS = [
    # "https://www.youtube.com/watch?v=aircAruvnKk",
    # "https://www.youtube.com/watch?v=wjZofJX0v4M",
    "https://www.youtube.com/watch?v=fHF22Wxuyw4",
    # "https://www.youtube.com/watch?v=C6YtPJxNULA",
]

for url in VIDEO_URLS:
    fetch_and_save_transcript(url)
    time.sleep(15)   # 🔥 increase delay


def process_vtt_files(raw_dir="data/raw", processed_dir="data/processed"):
    os.makedirs(processed_dir, exist_ok=True)

    for file in os.listdir(raw_dir):
        if file.endswith(".vtt"):
            file_path = os.path.join(raw_dir, file)

            # 🔥 Parse
            parsed = parse_vtt_to_json(file_path)

            # 🧹 Clean
            cleaned = clean_transcript(parsed)

            # 💾 Save
            output_path = os.path.join(processed_dir, file.replace(".vtt", ".json"))

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(cleaned, f, indent=4)

            print(f"✅ Processed: {output_path}")


process_vtt_files()