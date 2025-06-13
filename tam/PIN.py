# import requests
# import os
# import re

# # Your cookies and headers
# cookies = {
#     '_auth': '1',
#     '_pinterest_sess': 'TWc9PSZzNWZrVW9raU1ocndxbE91dFA2TUJSK0dZRnRQeHlPQU1qNGcwbkNlenEyVzlOeGpKVUIxNDc3a1RPYVIzdFFSb1h2Yk54NGxHOHNZM2ZBS2lTR3BIMHI0c3p0dGVOT2RNbHkvb2FRUERvREM1VDAxbjVCQitoMHJxdGxTb0RKWjdnSHVSaGFzYWhSTU1DZ0RXRms3MmR0SkJVYVJUVXJwN2ZMV2xhenJMSGNwcUxldDk5Q0syQmtwYkZ6OExEV0hITW53K2s3cW5haEpaNmJsQUJ5V0ZGcWZHL3pDV1l3MWdxWWlKSjM4OEtWZkFPYjBhQTU2emV3aFZFU1dNcW56dXlDRElIWDNyaXpkY0htM0tVZ2hWVlhNWWxqU3NlMVFxdDN6c0ZjUWFjZndGeVlHUUdsZnM3b1d5d3lFNHVCd0p1RVNuOGorL0VuakxNbXV3MGhVOVVJS2VwWVpnKzhwU0VkZlBNLytpVlcvSXJwRG9ROE5SOERVRW5EUTk5Qy85NGVOajhhc3h2ZHFKa1dhMHFhcWNTYjlUTE5GYU1Ydk1DdjZwTHoveVREYW1vck5UMGNTV2lFMHhMRVFKeDVnYkZETW15VDk5dzh3dXcycUdHK2drSTQ2RHhIclJuV3I3eERyMjd4SDB2OTI4cUVLQm5CdkJrUHRwWjVNOGZjSHBOSENzZ1p5U0d4czYwa0xFeFN2RS9MMEFmY25qWllaUk4wcjExdDRkeFkrZnBZMGpESXYzalVpN0NCK1R0WWJHdS9ISk1rQkEvWU9KY0V0d01nblR1ZXJyZTN1eWpETFhTYVFyc2tTR2s5MFlLTUxwZkNuaFNMSTcvRHFXS25OSkIyMEVMOGk2ME5YWFlKNGprMFNHcnRiNUlUSzc1LzVMNmd0bWw5a2Z1R25yRFJQT3ZpVmUwVk43YXZuVkthSW1uVXhXOTFqWGEzRVB2NGNyNnRBK2Y5dHJKb1lhVjdMNWdVNmcrcGtyQ3Z4Yyt1dWpLSi9PQ2NwMnlEVVNNbVNkcXl6b0oyWTNGYTJxeUVXa3Rpa3ozQ2RqOHpuWnZUcU1GaGlhc0dnTXNUVXlTTFVCdllpaWUyU3NWcHRXd1lLdUErUW96WDZuaTF5MkNwTkRxdkZOcDQ3K0tEenoxemF4YXJGUzhzYXgzV2h3SWxZTWNmWEVjekx0TVVaRUJQNkh1eE1mdmVCaUxINmFiVHZ6cUZ6UmRIOFR4V1gxSHBmS0JUR1JqVGpQeUVMRDZ5NDFZRzlsUDJ0eEdENVRtSDB5MGNLbjNXakM4YVBVYWZtVDV0Zm53QTFDOWJpTVpLVHBpRlRjU01MOHRMeGFQSlJlUTJqa2lIUEpzK3QrbzErbG5DTjlQS3VjRGhYQ3pUTzVHcllWNmkyOS9HUWxxU0pHa3pUbzVvNVd0RUVrTHMwOTFzWCtPMG8zTGtGWUJMZXZUYnZrNHhXakIwZGVUTG5iWVgvWUUvQ3pmczUyYUNiZDRNQjl2MGdod2htTGpaekF1YklmRE55eVVyTVdYdmpxVzFOSUEzdWI0aW1OalQvdWpFYzF4ZGJUNEFaQ0l0RG9DR1BYUDBkRDhheGlKeHJXOUd2YUhUTjhWVGlIeGQyMGNXL043ck1JbTJMQUlrRXJkY3Y2S0lWRW9vNW0zY1BsckVFeUl3bkFRdmdid2xNcy9ZUS9KODhpQU1nYmJndzdFMmVnQmtyVjFYeEpSVG1DdDJYRjhrdnlNMGFlRWc4ZWtOclhWZDI5WG1yZW1DVUhNREF6NFRpWXhSZlRKYjMmaFQwRllJTjNUUWFsQXROWXc2MGN3UnVINDBJPQ==',
#     '__Secure-s_a': 'OS8rdjRTOTJWR3FTMFp3ZEt0NFhnK09tS2RxOHp3QzI3L2NLUnkvWXRqU3JkcGVRbVdmU0tmSTFYdU1sWjdBN2FsYU1JN0hTczlkL0JkbzkxOUhCcGtJTVlmeVkydWVLZHo0V0g5am5qR09ZeWxjWTAyc29SeXJyMVA2eUUyMzlrelorYzNEamIrVzB2dkNybm9mV0dvR2MySlBwSzYxMElOVFVld3ROb0paNk1TZDQ5OWYwTS9kbnFVZkxPb2FsVFNpdGRqQlJCVE9RNkVmZEh4bHdiTTJEN2RRcVgyS0ZvbVZzMm4vYVNoblFRekVIL1dSL0ZtYkhTakNmQjZzMDZyQTF3K0VYUVJKcHpJcWFPbzNjVU9KakdCL2ZhWXdCQWNVN1RpaWtwTEwvWm05RUw0aVFkWkNTbVlEWjJ4UkJ0dkk0MUR1V0M1MllpUzVwQjdEbFgzaXVmVTloM0ZaaDEzS25DWVdyK3hzdmlZNmJySUYvYWd0UHZCd2djWDRFalgrUVdCUWF4WTZKQXNjaTlmdHZIbGNtY1JYWTZtZlVYN3JCWWtRbUZjV1BGOTlFbmJxVnZrSVlPOWJnRWNiZi9FcFdmbFhDay96T2xRa0QzdUorSDdvSjZjMkxkU0ptakRYQ202RWxaSXZBWDJKbG1nRDhiYnk5Y2hGSSs1MFMvUXE3bUlxZE0vNUN5NTBReVdLcHBnd1NaYUtnbnVyZk5uWVNaYTJSRjFFQTVPYkxDd0xjWEtRZWF3Q3duSENBY0txOVByQ3c0Yys1REU5eDFGZGRIVU10eWhXb2JMaTZWeUhXYUhRdkhBYmVFY3dKWkRjbk9pNTgwZHFhMGlHUDFsZ0ZJaEhjQ3RxUzZnZWRFS0Nudnkxa3ozNHpkWWsreWNITWlyTVV3RFBYNVVvL2lmS1FXUG5qMEg5NWoralhvVlZpTm9UNUJuQ0F6MEg1REVBdE12ZUd5eFUxTHZlUGNVYXl4Mks5OXJlSWs2SUF0WUZMZFF3TzN6Lzd4ZjNhcTJ2UTMxbVpWZDJRaUFJYkk0VTAyb3MrVFl3Q25NZ1lSNjc4TXMrL2RTZmN0Ym1pRmc4R1VtSENLTmZLK2hNMFFIb296SzhDWFZKclJ3ZVgyVGNQNGFlelcraUsrVlpTWU8rVlZYUFJIQ1FsWVFLeG5RN0NFNzduSkNiK0djSTNJNVI4bVRSMG9waXBmM3dMZ0NHdVhUaWRqcm9ab1lDcUhYeDRyYkJPeGplelFLcHlpd21kbDZCU2tVTVQ0N0VHOXJuZTlZVWEzdExzbHgxUG5VeVpJYlNlTkxxNm9QbVkvWm1ndlJ5MTV1QT0mRmkzdUdyM3VSRmZFbE9la2d6clhNaVdUQ1M0PQ==',
#     '_b': "AYknvI+xb9lLzpKUVmmASzWE/zgJHRql8TlP3adaqGiP4k8RONK2qFzc5fCKlBLNLpw=",
#     'csrftoken': 'YOUR_CSRF_TOKEN',
#     'ar_debug': '1',
#     '_routing_id': "b71b0d2e-7744-417d-aa7b-2f7da75436ce",
#     'sessionFunnelEventLogged': '1',
# }

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
#     'accept': 'application/json, text/javascript, */*; q=0.01',
#     'x-requested-with': 'XMLHttpRequest',
#     'x-csrftoken': cookies['csrftoken'],
# }

# # Replace this with the username and board you want to scrape
# username = "sunnychandu7227"
# board_slug = "milfy-actress"

# # Pinterest board API endpoint
# api_url = f"https://www.pinterest.com/{username}/{board_slug}.json"

# # Directory to save images
# os.makedirs(board_slug, exist_ok=True)

# # Helper function to download image
# def download_media(url, folder):
#     filename = os.path.join(folder, url.split('/')[-1].split('?')[0])
#     if not os.path.exists(filename):
#         try:
#             response = requests.get(url)
#             with open(filename, 'wb') as f:
#                 f.write(response.content)
#             print(f"Downloaded {filename}")
#         except Exception as e:
#             print(f"Error downloading {url}: {e}")

# # Scrape logic
# def scrape_board():
#     next_bookmark = None
#     while True:
#         params = {"data": {"options": {"board_id": None, "page_size": 25}}}
#         if next_bookmark:
#             params["data"]["options"]["bookmarks"] = [next_bookmark]

#         response = requests.get(api_url, headers=headers, cookies=cookies)
#         if response.status_code != 200:
#             print("Failed to load board")
#             print(response.text)
#             break

#         try:
#             data = response.json()
#         except Exception as e:
#             print(f"Failed to parse JSON: {e}")
#             break

#         pins = re.findall(r'"url":"(https://i\.pinimg\.com/[^"]+)"', response.text)
#         for pin_url in pins:
#             pin_url = pin_url.replace('\\u002F', '/')
#             download_media(pin_url, board_slug)

#         # Pagination
#         next_bookmark = data.get("resource", {}).get("options", {}).get("bookmarks", [None])[0]
#         if not next_bookmark or next_bookmark == "-end-":
#             break

# scrape_board()


import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIG ---
BOARD_URL = 'https://www.pinterest.com/USERNAME/BOARDNAME/'  # Replace with the real board URL
SCROLL_TIMES = 10  # Number of times to scroll down

# --- SETUP SELENIUM ---
options = Options()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- LOAD PAGE ---
driver.get(BOARD_URL)
time.sleep(3)

# --- SCROLL TO LOAD CONTENT ---
for _ in range(SCROLL_TIMES):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# --- PARSE PAGE SOURCE ---
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# --- FIND IMAGE URLS ---
img_tags = soup.find_all("img")
img_urls = set()

for tag in img_tags:
    src = tag.get("src")
    if src and "i.pinimg.com" in src:
        img_urls.add(src)

print(f"Found {len(img_urls)} image URLs")

# --- DOWNLOAD IMAGES ---
os.makedirs("pinterest_images", exist_ok=True)

for idx, img_url in enumerate(img_urls):
    try:
        response = requests.get(img_url)
        if response.status_code == 200:
            parsed = urlparse(img_url)
            filename = os.path.basename(parsed.path)
            file_path = os.path.join("pinterest_images", filename)

            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {img_url}: {e}")
