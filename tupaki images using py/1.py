import requests

headers = {
    'Referer': 'https://www.tupaki.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

base_url = 'https://www.tupaki.com/search'
query = 'sunny leone'

html_output = ""

for page in range(1, 30): 
    params = {
        'search': query,
        'search_type': 'all',
        'page': str(page),
    }

    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code == 200:
        html_output += f"\n<!-- Page {page} -->\n"
        html_output += response.text
    else:
        html_output += f"\n<!-- Failed to fetch page {page}. Status code: {response.status_code} -->\n"


with open("tupaki_search_results.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("Saved HTML content to tupaki_search_results.html")
