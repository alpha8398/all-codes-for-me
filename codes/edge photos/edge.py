import requests
import os

# Read URLs from a file
with open("image_urls.txt", "r") as f:
    urls = [line.strip() for line in f if line.strip()]

os.makedirs("downloaded_images", exist_ok=True)

for i, url in enumerate(urls):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        ext = url.split('.')[-1].split('?')[0][:4]  # Get extension safely
        filename = f"downloaded_images/image_{i+1}.{ext if ext.isalpha() else 'jpg'}"
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"✅ Downloaded: {filename}")
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
