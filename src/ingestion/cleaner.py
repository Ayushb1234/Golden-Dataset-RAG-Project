import re


def clean_text(text):
    # remove filler & noise
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"\(.*?\)", "", text)

    # remove repeated spaces
    text = re.sub(r"\s+", " ", text)

    # remove weird chars
    text = re.sub(r"[^a-zA-Z0-9.,!? ]", "", text)

    return text.strip()


def clean_transcript(transcript_json):
    cleaned_data = []

    prev_text = ""

    for entry in transcript_json:
        text = clean_text(entry["text"])

        # ❗ remove duplicates (very common in subtitles)
        if text and text != prev_text:
            cleaned_data.append({
                "text": text,
                "start": entry["start"],
                "duration": entry["duration"]
            })

            prev_text = text

    return cleaned_data