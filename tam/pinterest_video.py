import requests
from bs4 import BeautifulSoup
import json
import re

pin_url = "https://in.pinterest.com/pin/71705819062094054/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Step 1: Fetch the pin page
response = requests.get(pin_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find the JSON-LD script tag that contains the video URL
scripts = soup.find_all("script", type="application/ld+json")

video_url = None

for script in scripts:
    try:
        data = json.loads(script.string)
        if isinstance(data, dict) and "contentUrl" in data:
            video_url = data["contentUrl"]
            break
    except json.JSONDecodeError:
        continue

if video_url:
    print(f"Video URL found: {video_url}")
    video_data = requests.get(video_url, headers=headers).content

    filename = "pinterest_video_2.mp4"
    with open(filename, "wb") as f:
        f.write(video_data)
    print(f"Downloaded video to: {filename}")
else:
    print("Video URL not found.")
