# import re
# import requests
# from urllib.parse import urljoin
# from bs4 import BeautifulSoup

# # Replace with your actual URL
# url = "https://cdn.pornkeen.net/2022/12/20/"

# # Get the response
# response = requests.get(url)
# content = response.text

# # Parse the HTML content
# soup = BeautifulSoup(content, "html.parser")

# # Extract all href links
# all_links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

# filtered_links = [link for link in all_links if re.search(r'aish', link, re.IGNORECASE)]


# print(',\n'.join(f'"{link}"' for link in filtered_links))



import re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# List of URLs to process
urls = [
"https://cdn.pornkeen.net/2022/12/14/",
"https://cdn.pornkeen.net/2022/12/15/",
"https://cdn.pornkeen.net/2022/12/16/",
"https://cdn.pornkeen.net/2022/12/17/",
"https://cdn.pornkeen.net/2022/12/18/",
"https://cdn.pornkeen.net/2022/12/19/",
"https://cdn.pornkeen.net/2022/12/20/",
"https://cdn.pornkeen.net/2022/12/21/",
"https://cdn.pornkeen.net/2022/12/22/",
"https://cdn.bollyxxx.net/2022/11/22/",
"https://cdn.bollyxxx.net/2022/11/23/",
"https://cdn.bollyxxx.net/2022/11/24/",
"https://cdn.bollyxxx.net/2022/11/25/",
"https://cdn.bollyxxx.net/2022/11/26/",
"https://cdn.bollyxxx.net/2022/11/27/",
"https://cdn.bollyxxx.net/2022/11/28/",
"https://cdn.bollyxxx.net/2022/11/29/",
"https://cdn.bollyxxx.net/2022/11/30/",
"https://cdn.bollyxxx.net/2022/11/31/",
"https://cdn.bollyxxx.net/2022/11/32/",
"https://cdn.bollyxxx.net/2022/11/33/",
"https://cdn.bollyxxx.net/2022/11/34/",
"https://cdn.bollyxxx.net/2022/11/35/",
"https://cdn.bollyxxx.net/2022/11/36/",
"https://cdn.bollyxxx.net/2022/11/37/",
"https://cdn.bollyxxx.net/2022/11/38/",
"https://cdn.bollyxxx.net/2024/01/01/",



]

# To store all matching links
all_matching_links = set()

# Loop through each URL
for url in urls:
    try:
        response = requests.get(url, timeout=10)
        content = response.text

        # Parse HTML
        soup = BeautifulSoup(content, "html.parser")

        # Extract and normalize all href links
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

        # Filter links containing 'rai' or 'aish' (case-insensitive)
        matches = [link for link in links if re.search(r'anushka', link, re.IGNORECASE)]

        all_matching_links.update(matches)

    except Exception as e:
        print(f"Failed to process {url}: {e}")

# Output the final list in the desired format
print(',\n'.join(f'"{link}"' for link in sorted(all_matching_links)))
