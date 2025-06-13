# import requests

# cookies = {
#     'IGNORE_INTERSTITIAL': '1',
#     'source': 'desktop',
#     '_ga_store': '!%2540%2523%2524%2525%255E%2526*%2540%2523%2524%255E%2525%2526(*)(%2526%2524%2525%2526%255E*%253D%253D%2523%25231003096',
# }

# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
#     'accept-language': 'en-US,en;q=0.8',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'IGNORE_INTERSTITIAL=1; source=desktop; _ga_store=!%2540%2523%2524%2525%255E%2526*%2540%2523%2524%255E%2525%2526(*)(%2526%2524%2525%2526%255E*%253D%253D%2523%25231003096',
#     'if-none-match': '0.43227528709565854',
#     'priority': 'u=0, i',
#     'referer': 'https://www.tupaki.com/',
#     'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Brave";v="132"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'sec-gpc': '1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
# }

# response = requests.get(
#     'https://www.tupaki.com/photogallery/rashmika-mandana-glamorous-clicks-1408170',
#     cookies=cookies,
#     headers=headers,
# )
# print(response.text)

import requests
import json

cookies = {
    'IGNORE_INTERSTITIAL': '1',
    'source': 'desktop',
    '_ga_store': '!%2540%2523%2524%2525%255E%2526*%2540%2523%2524%255E%2525%2526(*)(%2526%2524%2525%2526%255E*%253D%253D%2523%25231003096',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'max-age=0',
    'if-none-match': '0.43227528709565854',
    'priority': 'u=0, i',
    'referer': 'https://www.tupaki.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Brave";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.tupaki.com/photogallery/rashmika-mandana-glamorous-clicks-1408170',
    cookies=cookies,
    headers=headers,
)

# Extract URLs containing "content.tupaki.com/tupaki"
if response.status_code == 200:
    content = response.text
    if "content.tupaki.com/tupaki" in content:
        print(json.dumps({"content": content}, indent=4))
    else:
        print("No matching content found.")
else:
    print(f"Failed to fetch page, status code: {response.status_code}")
