import re


def time_to_seconds(t):
    """Convert VTT timestamp to seconds (robust)"""

    # remove extra stuff like 'align:start position:0%'
    t = t.strip().split(" ")[0]

    parts = t.split(":")

    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h = 0
        m, s = parts
    else:
        raise ValueError(f"Invalid timestamp format: {t}")

    if "." in s:
        s, ms = s.split(".")
        ms = int(ms)
    else:
        ms = 0

    return int(h)*3600 + int(m)*60 + int(s) + ms/1000

def parse_vtt_to_json(file_path):
    data = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if "-->" in line:
            start, end = line.split(" --> ")
            start_sec = time_to_seconds(start)
            end_sec = time_to_seconds(end)

            text = lines[i+1].strip() if i+1 < len(lines) else ""

            data.append({
                "text": text,
                "start": start_sec,
                "duration": end_sec - start_sec
            })

            i += 2
        else:
            i += 1

    return data