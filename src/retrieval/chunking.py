def chunk_transcript(transcript, chunk_size=150, overlap=30):
    """
    transcript: list of {text, start, duration}
    returns: list of chunks with metadata
    """

    chunks = []
    current_chunk = []
    current_words = 0

    for entry in transcript:
        words = entry["text"].split()
        current_chunk.append(entry)
        current_words += len(words)

        if current_words >= chunk_size:
            chunk_text = " ".join([e["text"] for e in current_chunk])

            chunks.append({
                "text": chunk_text,
                "start": current_chunk[0]["start"],
                "end": current_chunk[-1]["start"] + current_chunk[-1]["duration"]
            })

            # 🔁 overlap handling
            current_chunk = current_chunk[-overlap:]
            current_words = sum(len(e["text"].split()) for e in current_chunk)

    return chunks