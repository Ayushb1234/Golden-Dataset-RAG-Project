import os
import json
import subprocess
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be" in url:
        return url.split("/")[-1]
    return url
import time
import subprocess

def fetch_with_ytdlp(video_url, video_id, output_dir):
    for attempt in range(3):   # retry 3 times
        try:
            print(f"⚠️ yt-dlp attempt {attempt+1}")

            command = [
                "yt-dlp",
                "--write-auto-sub",
                "--sub-lang", "en,hi",
                "--skip-download",
                "-o", f"{output_dir}/{video_id}",
                video_url
            ]

            subprocess.run(command, check=True)
            print(f"✅ yt-dlp subtitles downloaded for {video_id}")
            return

        except Exception as e:
            print(f"❌ attempt {attempt+1} failed: {e}")
            time.sleep(20)   # wait before retry

    print(f"💀 yt-dlp completely failed for {video_id}")


def fetch_and_save_transcript(video_url, output_dir="data/raw"):
    video_id = extract_video_id(video_url)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en','hi'])

        transcript_data = [
            {
                "text": entry["text"],
                "start": entry["start"],
                "duration": entry["duration"]
            }
            for entry in transcript
        ]

        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, f"{video_id}.json")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(transcript_data, f, indent=4)

        print(f"✅ Saved transcript (API): {file_path}")

    except Exception as e:
        print(f"❌ API failed: {e}")
        fetch_with_ytdlp(video_url, video_id, output_dir)