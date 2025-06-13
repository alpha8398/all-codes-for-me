import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_album_images(album_url, cookies, headers):
    # Use part of the URL as folder name, sanitize it
    parsed_url = urlparse(album_url)
    folder_name = parsed_url.path.strip('/').replace('/', '_')
    # Include query parameters to distinguish pages if needed
    if parsed_url.query:
        safe_query = parsed_url.query.replace('&', '_').replace('=', '-').replace('%', '')
        folder_name += '_' + safe_query
    save_dir = f'downloads/{folder_name}'
    os.makedirs(save_dir, exist_ok=True)

    response = requests.get(album_url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img', loading=True)

    for i, img in enumerate(img_tags, start=1):
        src = img.get('src')
        if src:
            full_img_url = urljoin(album_url, src)
            file_ext = full_img_url.split('.')[-1].split('?')[0]
            file_name = f'image_{i:03d}.{file_ext}'
            file_path = os.path.join(save_dir, file_name)

            try:
                img_data = requests.get(full_img_url).content
                with open(file_path, 'wb') as f:
                    f.write(img_data)
                print(f'Downloaded: {file_name}')
            except Exception as e:
                print(f'Failed to download {full_img_url}: {e}')


# List of album URLs (not a string)
album_urls = [

"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=19&seek=2017-09-28%2018%3A27%3A15.LUE",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=18&seek=2019-07-16%2018%3A01%3A45.7Ht",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=17&seek=2019-07-16%2018%3A07%3A18.7Hg",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=16&seek=2019-07-16%2018%3A12%3A13.7Sz",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=15&seek=2019-07-16%2018%3A12%3A31.7Sq",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=14&seek=2019-07-16%2018%3A22%3A29.7o9",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=13&seek=2019-07-16%2018%3A22%3A40.7oC",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=12&seek=2019-07-16%2018%3A36%3A04.7rR",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=11&seek=2019-07-16%2018%3A36%3A10.7rX",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=10&seek=2019-07-16%2018%3A36%3A16.7sf",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=9&seek=2019-07-16%2018%3A46%3A35.7sk",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=8&seek=2019-07-16%2018%3A46%3A42.7L3",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=7&seek=2019-07-16%2018%3A46%3A47.7LI",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=6&seek=2019-07-16%2018%3A46%3A53.7QD",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=5&seek=2019-07-16%2018%3A55%3A33.7Q6",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=4&seek=2019-07-16%2018%3A55%3A40.7ZB",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=3&seek=2019-07-16%2018%3A59%3A13.7Ze",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=2&seek=2019-10-17%2005%3A31%3A31.Rgc",
"https://imgfy.net/me/search/?list=images&q=sunny%20leone&sort=date_desc&page=1",
"https://imgfy.net/album/Hot-Sunny-Leone-Instagram-Photos.s",

]

cookies = {
    'PHPSESSID': '3abqpd6qnfj7kbf26aev4devuo',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'max-age=0',
    'referer': 'https://imgfy.net/image/4d9P',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

for url in album_urls:
    download_album_images(url, cookies, headers)
