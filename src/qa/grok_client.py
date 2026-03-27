import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")


def query_grok(prompt):
    url = "https://api.x.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "grok-1",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    # 🔥 DEBUG PRINT (important)
    print("Grok raw response:", result)

    if "choices" not in result:
        raise Exception(f"Grok API error: {result}")

    return result["choices"][0]["message"]["content"]