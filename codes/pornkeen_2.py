from bs4 import BeautifulSoup
import os

folder_path = "."  # directory with .html files
collected_links = []

for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            meta_tag = soup.find("meta", itemprop="contentURL")
            if meta_tag:
                video_url = meta_tag.get("content")
                if video_url:
                    collected_links.append(video_url)
                    print(f"Found in {filename}: {video_url}")
            else:
                print(f"No video <meta> found in {filename}")

# Optional: save to text file
with open("video_links.txt", "w", encoding="utf-8") as f:
    for link in collected_links:
        f.write(link + "\n")
