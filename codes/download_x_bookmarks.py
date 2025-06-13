# # # # # import os
# # # # # import json
# # # # # import subprocess
# # # # # import time
# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.chrome.service import Service
# # # # # from selenium.webdriver.common.by import By
# # # # # from selenium.webdriver.chrome.options import Options

# # # # # # === Step 1: Config file setup ===
# # # # # config = {
# # # # #     "extractor": {
# # # # #         "twitter": {
# # # # #             "cookies": {
# # # # #                 "auth_token": "e893a19c85fd2700624e2e98d9512ec532484dff",
# # # # #                 "ct0":"83e27f861fc91304666479b15910c21395988d33ddeaef2a73f42f601ccd17f555e1e55e9f8c56d81d3b8d62bae64c71a999f27e53074b340139d47dea7211b6ca50167ece6d1b9c8b57f37894fd1cd3"
# # # # #             },
# # # # #             "original": True,
# # # # #             "retweets": False,
# # # # #             "replies": True,
# # # # #             "videos": True
# # # # #         }
# # # # #     },
# # # # #     "downloader": {
# # # # #         "part": False,
# # # # #         "overwrite": False
# # # # #     },
# # # # #     "output": r"C:\hpswsetup\sp108788\Actress\Phoyos"
# # # # # }

# # # # # # Save the config to gallery-dl's config path
# # # # # config_path = os.path.join(os.path.expanduser('~'), 'gallery-dl.conf')

# # # # # with open(config_path, 'w') as f:
# # # # #     json.dump(config, f, indent=4)

# # # # # print(f"[+] Config saved to {config_path}")

# # # # # # === Step 2: Download Twitter bookmarks ===
# # # # # gallery_dl_exe = r"C:/Users/gayat/AppData/Roaming/Python/Python311/Scripts/gallery-dl.exe"

# # # # # try:
# # # # #     print("[*] Starting download of your X Bookmarks...")
# # # # #     subprocess.run([gallery_dl_exe, 'https://twitter.com/i/bookmarks'], check=True)
# # # # #     print("[✓] Download complete!")

# # # # #     # === Step 3: Auto-Unbookmark using Selenium ===
# # # # #     print("[*] Starting unbookmarking process...")

# # # # #     # Your ChromeDriver path
# # # # #     CHROMEDRIVER_PATH = r"C:/Users/gayat/.wdm/drivers/chromedriver/win64/135.0.7049.42/chromedriver-win32/chromedriver.exe"
# # # # #     auth_token = config["extractor"]["twitter"]["cookies"]["auth_token"]

# # # # #     # Setup Chrome options
# # # # #     options = Options()
# # # # #     options.add_argument("--headless")  # Run in background; comment out to watch
# # # # #     options.add_argument("--disable-blink-features=AutomationControlled")
# # # # #     options.add_argument("--window-size=1920,1080")

# # # # #     service = Service(CHROMEDRIVER_PATH)
# # # # #     driver = webdriver.Chrome(service=service, options=options)

# # # # #     # Step A: Visit Twitter to match domain before setting cookie
# # # # #     driver.get("https://twitter.com/")
# # # # #     time.sleep(3)  # Allow initial page load

# # # # #     # Step B: Inject auth_token as cookie
# # # # #     driver.add_cookie({
# # # # #         "name": "auth_token",
# # # # #         "value": auth_token,
# # # # #         "domain": ".twitter.com",
# # # # #         "path": "/",
# # # # #         "secure": True,
# # # # #         "httpOnly": True,
# # # # #     })

# # # # #     # Step C: Go directly to bookmarks page
# # # # #     driver.get("https://twitter.com/i/bookmarks")
# # # # #     time.sleep(5)  # Allow bookmarks to load

# # # # #     # === Step D: Loop to unbookmark all ===
# # # # #     total_unbookmarked = 0
# # # # #     while True:
# # # # #         unbookmark_buttons = driver.find_elements(By.XPATH, "//div[@data-testid='unbookmark']")
# # # # #         if not unbookmark_buttons:
# # # # #             # Scroll to load more bookmarks
# # # # #             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # # # #             time.sleep(3)  # Wait for more content
# # # # #             unbookmark_buttons = driver.find_elements(By.XPATH, "//div[@data-testid='unbookmark']")
# # # # #             if not unbookmark_buttons:
# # # # #                 break  # No more bookmarks found, exit loop

# # # # #         for btn in unbookmark_buttons:
# # # # #             try:
# # # # #                 driver.execute_script("arguments[0].scrollIntoView(true);", btn)
# # # # #                 btn.click()
# # # # #                 total_unbookmarked += 1
# # # # #                 time.sleep(1)  # Avoid rate limits
# # # # #             except Exception as e:
# # # # #                 print(f"[!] Error clicking unbookmark: {e}")

# # # # #         time.sleep(2)  # Give time for page to stabilize

# # # # #     print(f"[✓] Unbookmarking finished! Total removed: {total_unbookmarked}")
# # # # #     driver.quit()

# # # # # except subprocess.CalledProcessError as e:
# # # # #     print(f"[!] Download failed: {e}")
# # # # # except FileNotFoundError:
# # # # #     print(f"[!] gallery-dl executable not found at: {gallery_dl_exe}")
# # # # # except Exception as ex:
# # # # #     print(f"[!] Something went wrong: {ex}")


# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.chrome.options import Options
# # # # # from selenium.webdriver.common.by import By
# # # # # import time

# # # # # # === 🔧 Your Twitter Cookies Here ===
# # # # # cookies = [
# # # # #     {"name": "auth_token", "value": "e893a19c85fd2700624e2e98d9512ec532484dff"},
# # # # #     {"name": "ct0", "value": "83e27f861fc91304666479b15910c21395988d33ddeaef2a73f42f601ccd17f555e1e55e9f8c56d81d3b8d62bae64c71a999f27e53074b340139d47dea7211b6ca50167ece6d1b9c8b57f37894fd1cd3"},
# # # # #     {"name": "guest_id", "value": "PASTE_IF_NEEDED"}
# # # # # ]

# # # # # # === ✅ Configure WebDriver ===
# # # # # options = Options()
# # # # # # Comment out below to see browser window
# # # # # options.add_argument("--headless")
# # # # # options.add_argument("--disable-blink-features=AutomationControlled")
# # # # # driver = webdriver.Chrome(options=options)

# # # # # # === 🌐 Step 1: Open Twitter homepage to set cookies ===
# # # # # driver.get("https://twitter.com")
# # # # # time.sleep(3)

# # # # # # === 🍪 Step 2: Inject Cookies ===
# # # # # for cookie in cookies:
# # # # #     driver.add_cookie({
# # # # #         "name": cookie["name"],
# # # # #         "value": cookie["value"],
# # # # #         "domain": ".twitter.com",
# # # # #         "path": "/"
# # # # #     })

# # # # # # === 📖 Step 3: Go to Bookmarks Page ===
# # # # # driver.get("https://twitter.com/i/bookmarks")
# # # # # time.sleep(5)

# # # # # # === 🔁 Step 4: Scroll to Load More Bookmarks ===
# # # # # for _ in range(300):
# # # # #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # # # #     time.sleep(2)

# # # # # # === 🔍 Step 5: Extract Tweet URLs ===
# # # # # tweet_links = set()
# # # # # elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/status/')]")
# # # # # for el in elements:
# # # # #     href = el.get_attribute("href")
# # # # #     if href and "/status/" in href:
# # # # #         tweet_links.add(href.split("?")[0])  # remove tracking params

# # # # # # === 💾 Step 6: Save to File ===
# # # # # with open("tweets.txt", "w", encoding="utf-8") as f:
# # # # #     for link in sorted(tweet_links):
# # # # #         f.write(link + "\n")

# # # # # print(f"[✔] Extracted {len(tweet_links)} tweet links from your bookmarks.")
# # # # # driver.quit()


# # # # # # # # # # # # import json
# # # # # # # # # # # # import time
# # # # # # # # # # # # from selenium import webdriver
# # # # # # # # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # # # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # # # # # # # from selenium.webdriver.common.by import By

# # # # # # # # # # # # # === Step 1: Load Cookies from File ===
# # # # # # # # # # # # def load_cookies(filepath):
# # # # # # # # # # # #     with open(filepath, "r", encoding="utf-8") as f:
# # # # # # # # # # # #         return json.load(f)

# # # # # # # # # # # # # === Step 2: Setup Chrome Driver ===
# # # # # # # # # # # # def create_driver():
# # # # # # # # # # # #     chrome_options = Options()
# # # # # # # # # # # #     chrome_options.add_argument("--start-maximized")
# # # # # # # # # # # #     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
# # # # # # # # # # # #     service = Service()  # Automatically finds chromedriver if in PATH
# # # # # # # # # # # #     driver = webdriver.Chrome(service=service, options=chrome_options)
# # # # # # # # # # # #     return driver

# # # # # # # # # # # # # === Step 3: Load Twitter and Inject Cookies ===
# # # # # # # # # # # # def login_with_cookies(driver, cookies):
# # # # # # # # # # # #     driver.get("https://twitter.com")  # MUST load domain before adding cookies
# # # # # # # # # # # #     time.sleep(3)  # Allow site to load
    
# # # # # # # # # # # #     for cookie in cookies:
# # # # # # # # # # # #         # Remove domain to avoid InvalidCookieDomainException
# # # # # # # # # # # #         cookie = cookie.copy()
# # # # # # # # # # # #         cookie.pop("domain", None)
# # # # # # # # # # # #         try:
# # # # # # # # # # # #             driver.add_cookie(cookie)
# # # # # # # # # # # #         except Exception as e:
# # # # # # # # # # # #             print(f"Error adding cookie {cookie.get('name')}: {e}")
    
# # # # # # # # # # # #     driver.get("https://twitter.com/i/bookmarks")  # Go to bookmarks after cookies added

# # # # # # # # # # # # # === Step 4: Optionally Download or Scrape Bookmarks ===
# # # # # # # # # # # # def scrape_bookmarks(driver):
# # # # # # # # # # # #     time.sleep(5)  # Wait for bookmarks to load
# # # # # # # # # # # #     tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    
# # # # # # # # # # # #     for i, tweet in enumerate(tweets[:10], 1):  # Limit to first 10 tweets for demo
# # # # # # # # # # # #         try:
# # # # # # # # # # # #             text = tweet.text
# # # # # # # # # # # #             print(f"\n--- Bookmark {i} ---\n{text}\n")
# # # # # # # # # # # #         except Exception as e:
# # # # # # # # # # # #             print(f"Error reading tweet {i}: {e}")

# # # # # # # # # # # # # === Main Execution ===
# # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # #     cookies = load_cookies("cookies.json")  # Replace with your actual file
# # # # # # # # # # # #     driver = create_driver()
    
# # # # # # # # # # # #     try:
# # # # # # # # # # # #         login_with_cookies(driver, cookies)
# # # # # # # # # # # #         scrape_bookmarks(driver)
# # # # # # # # # # # #     finally:
# # # # # # # # # # # #         input("\nPress Enter to exit and close browser...")
# # # # # # # # # # # #         driver.quit()


# # # # # # # # # # # import json
# # # # # # # # # # # import os
# # # # # # # # # # # import requests

# # # # # # # # # # # def load_cookies(file_path):
# # # # # # # # # # #     """Loads cookies from a JSON file with error checking."""
# # # # # # # # # # #     if not os.path.exists(file_path):
# # # # # # # # # # #         raise FileNotFoundError(f"Cookie file not found: {file_path}")

# # # # # # # # # # #     if os.path.getsize(file_path) == 0:
# # # # # # # # # # #         raise ValueError("The cookies.json file is empty.")

# # # # # # # # # # #     try:
# # # # # # # # # # #         with open(file_path, "r", encoding="utf-8") as f:
# # # # # # # # # # #             cookies = json.load(f)
# # # # # # # # # # #             return cookies
# # # # # # # # # # #     except json.JSONDecodeError as e:
# # # # # # # # # # #         raise ValueError(f"Invalid JSON format in {file_path}: {e}")

# # # # # # # # # # # def convert_cookies_to_dict(cookie_list):
# # # # # # # # # # #     """
# # # # # # # # # # #     Converts a list of cookie dictionaries (like from browser export)
# # # # # # # # # # #     into a requests-compatible cookie dictionary.
# # # # # # # # # # #     """
# # # # # # # # # # #     if isinstance(cookie_list, dict):
# # # # # # # # # # #         return cookie_list  # Already in dict format

# # # # # # # # # # #     cookie_dict = {}
# # # # # # # # # # #     for cookie in cookie_list:
# # # # # # # # # # #         if 'name' in cookie and 'value' in cookie:
# # # # # # # # # # #             cookie_dict[cookie['name']] = cookie['value']
# # # # # # # # # # #     return cookie_dict

# # # # # # # # # # # def main():
# # # # # # # # # # #     cookie_file = "cookies.json"  # Replace with the correct path if needed

# # # # # # # # # # #     try:
# # # # # # # # # # #         raw_cookies = load_cookies(cookie_file)
# # # # # # # # # # #         cookies = convert_cookies_to_dict(raw_cookies)

# # # # # # # # # # #         # Example request (replace with actual use case)
# # # # # # # # # # #         url = "https://example.com"
# # # # # # # # # # #         response = requests.get(url, cookies=cookies)

# # # # # # # # # # #         print("Response Status Code:", response.status_code)
# # # # # # # # # # #         print("Response Content:", response.text[:500])  # Preview first 500 chars

# # # # # # # # # # #     except Exception as e:
# # # # # # # # # # #         print("Error:", e)

# # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # #     main()
# # # # # # # # # # import requests
# # # # # # # # # # import os

# # # # # # # # # # def parse_netscape_cookies(file_path):
# # # # # # # # # #     """
# # # # # # # # # #     Parses a cookies.txt file in Netscape format into a dictionary
# # # # # # # # # #     compatible with requests.
# # # # # # # # # #     """
# # # # # # # # # #     if not os.path.exists(file_path):
# # # # # # # # # #         raise FileNotFoundError(f"Cookie file not found: {file_path}")

# # # # # # # # # #     cookies = {}
# # # # # # # # # #     with open(file_path, "r", encoding="utf-8") as f:
# # # # # # # # # #         for line in f:
# # # # # # # # # #             line = line.strip()
# # # # # # # # # #             if not line or line.startswith("#"):
# # # # # # # # # #                 continue  # Skip comments and blank lines

# # # # # # # # # #             parts = line.split("\t")
# # # # # # # # # #             if len(parts) == 7:
# # # # # # # # # #                 domain, flag, path, secure, expiry, name, value = parts
# # # # # # # # # #                 cookies[name] = value
# # # # # # # # # #             else:
# # # # # # # # # #                 raise ValueError("Invalid cookie format line: " + line)
# # # # # # # # # #     return cookies

# # # # # # # # # # def main():
# # # # # # # # # #     cookie_file = "x.com_cookies.txt"  # Path to your Netscape-format cookies

# # # # # # # # # #     try:
# # # # # # # # # #         cookies = parse_netscape_cookies(cookie_file)

# # # # # # # # # #         # Example request to x.com bookmarks
# # # # # # # # # #         url = "https://x.com/i/bookmarks"
# # # # # # # # # #         headers = {
# # # # # # # # # #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
# # # # # # # # # #         }

# # # # # # # # # #         response = requests.get(url, cookies=cookies, headers=headers)

# # # # # # # # # #         print("Response Status Code:", response.status_code)
# # # # # # # # # #         print("Response Text (preview):", response.text[:500])

# # # # # # # # # #     except Exception as e:
# # # # # # # # # #         print("Error:", e)

# # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # #     main()

# # # # # # # # # import requests

# # # # # # # # # def parse_netscape_cookies(file_path):
# # # # # # # # #     cookies = {}
# # # # # # # # #     with open(file_path, "r", encoding="utf-8") as f:
# # # # # # # # #         for line in f:
# # # # # # # # #             if not line.strip() or line.startswith("#"):
# # # # # # # # #                 continue
# # # # # # # # #             parts = line.strip().split("\t")
# # # # # # # # #             if len(parts) == 7:
# # # # # # # # #                 cookies[parts[5]] = parts[6]
# # # # # # # # #     return cookies

# # # # # # # # # def main():
# # # # # # # # #     cookie_file = "x.com_cookies.txt"
# # # # # # # # #     cookies = parse_netscape_cookies(cookie_file)

# # # # # # # # #     if 'auth_token' not in cookies or 'ct0' not in cookies:
# # # # # # # # #         print("Missing required cookies: 'auth_token' or 'ct0'")
# # # # # # # # #         return

# # # # # # # # #     headers = {
# # # # # # # # #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
# # # # # # # # #         "Accept": "*/*",
# # # # # # # # #         "Accept-Language": "en-US,en;q=0.9",
# # # # # # # # #         "X-Csrf-Token": cookies.get("ct0", ""),
# # # # # # # # #         "X-Twitter-Active-User": "yes",
# # # # # # # # #         "X-Twitter-Client-Language": "en",
# # # # # # # # #         "Referer": "https://x.com/",
# # # # # # # # #     }

# # # # # # # # #     # This is a placeholder; the real endpoint may be private or GraphQL-based
# # # # # # # # #     url = "https://twitter.com/i/bookmarks"  # Not guaranteed to work directly

# # # # # # # # #     response = requests.get(url, cookies=cookies, headers=headers)
# # # # # # # # #     print("Response Status Code:", response.status_code)
# # # # # # # # #     print("Response Preview:", response.text[:500])

# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     main()


# # # # # # # # import requests
# # # # # # # # import re

# # # # # # # # cookies = {
# # # # # # # #     'night_mode': '2',
# # # # # # # #     'kdt': 'ObXU3CF1ijADzvJQZDr03t8T2QewV4v16YlFn1R8',
# # # # # # # #     'auth_token': 'e893a19c85fd2700624e2e98d9512ec532484dff',
# # # # # # # #     'ct0': '83e27f861fc91304666479b15910c21395988d33ddeaef2a73f42f601ccd17f555e1e55e9f8c56d81d3b8d62bae64c71a999f27e53074b340139d47dea7211b6ca50167ece6d1b9c8b57f37894fd1cd3',
# # # # # # # #     'twid': 'u%3D1790358327974842368',
# # # # # # # #     'personalization_id': '"v1_CUAtJ+qa8XJ0da9Imv8i+g=="',
# # # # # # # #     'dnt': '1',
# # # # # # # #     'des_opt_in': 'Y',
# # # # # # # #     '_ga': 'GA1.2.1180435595.1716297519',
# # # # # # # #     '_ga_RJGMY4G45L': 'GS1.1.1745724145.2.0.1745724403.60.0.0',
# # # # # # # #     'ph_phc_TXdpocbGVeZVm5VJmAsHTMrCofBQu3e0kN8HGMNGTVW_posthog': '%7B%22distinct_id%22%3A%2201964709-4b2c-796e-a67f-99b9dfec9244%22%2C%22%24sesid%22%3A%5B1746364057238%2C%2201969b68-b7f4-75a3-963a-8e623d9a6a35%22%2C1746364053492%5D%7D',
# # # # # # # #     'guest_id_ads': 'v1%3A174784399256673946',
# # # # # # # #     'guest_id_marketing': 'v1%3A174784399256673946',
# # # # # # # #     'guest_id': 'v1%3A174784399256673946',
# # # # # # # #     'lang': 'en',
# # # # # # # #     '__cf_bm': '8zVW4fmTgHQV57KC4CU.OprjyymbAy7Rw79PLA7msmk-1748668293-1.0.1.1-uW5_Vud.EjwYQBLuDNDvtgyjrFO3bvQn2zc7QWBa7JgpsQTLZxPTF2PWvK1u8W96l0CPM4prpFJtp23YUJzOlgDe6tUyGe1ZL9goiwq_hoE',
# # # # # # # # }

# # # # # # # # headers = {
# # # # # # # #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# # # # # # # #     'accept-language': 'en-US,en;q=0.9',
# # # # # # # #     'cache-control': 'max-age=0',
# # # # # # # #     'priority': 'u=0, i',
# # # # # # # #     'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
# # # # # # # #     'sec-ch-ua-mobile': '?0',
# # # # # # # #     'sec-ch-ua-platform': '"Windows"',
# # # # # # # #     'sec-fetch-dest': 'document',
# # # # # # # #     'sec-fetch-mode': 'navigate',
# # # # # # # #     'sec-fetch-site': 'same-origin',
# # # # # # # #     'sec-fetch-user': '?1',
# # # # # # # #     'upgrade-insecure-requests': '1',
# # # # # # # #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
# # # # # # # #     # 'cookie': 'night_mode=2; kdt=ObXU3CF1ijADzvJQZDr03t8T2QewV4v16YlFn1R8; auth_token=e893a19c85fd2700624e2e98d9512ec532484dff; ct0=83e27f861fc91304666479b15910c21395988d33ddeaef2a73f42f601ccd17f555e1e55e9f8c56d81d3b8d62bae64c71a999f27e53074b340139d47dea7211b6ca50167ece6d1b9c8b57f37894fd1cd3; twid=u%3D1790358327974842368; personalization_id="v1_CUAtJ+qa8XJ0da9Imv8i+g=="; dnt=1; des_opt_in=Y; _ga=GA1.2.1180435595.1716297519; _ga_RJGMY4G45L=GS1.1.1745724145.2.0.1745724403.60.0.0; ph_phc_TXdpocbGVeZVm5VJmAsHTMrCofBQu3e0kN8HGMNGTVW_posthog=%7B%22distinct_id%22%3A%2201964709-4b2c-796e-a67f-99b9dfec9244%22%2C%22%24sesid%22%3A%5B1746364057238%2C%2201969b68-b7f4-75a3-963a-8e623d9a6a35%22%2C1746364053492%5D%7D; guest_id_ads=v1%3A174784399256673946; guest_id_marketing=v1%3A174784399256673946; guest_id=v1%3A174784399256673946; lang=en; __cf_bm=8zVW4fmTgHQV57KC4CU.OprjyymbAy7Rw79PLA7msmk-1748668293-1.0.1.1-uW5_Vud.EjwYQBLuDNDvtgyjrFO3bvQn2zc7QWBa7JgpsQTLZxPTF2PWvK1u8W96l0CPM4prpFJtp23YUJzOlgDe6tUyGe1ZL9goiwq_hoE',
# # # # # # # # }

# # # # # # # # response = requests.get('https://x.com/i/bookmarks', cookies=cookies, headers=headers)
# # # # # # # # if response.status_code == 200:
# # # # # # # #     # Extract URLs containing /status/
# # # # # # # #     # status_urls = re.findall(r'https://x\.com/\w+/status/\d+', response.text)
# # # # # # # #     status_urls = re.findall(r'https://(?:www\.)?x\.com/[^/]+/status/\d+', response.text)

# # # # # # # #     # Remove duplicates and print each
# # # # # # # #     for url in set(status_urls):
# # # # # # # #         # print(url)
# # # # # # # #         print(response.text[:2000])  # Print first 2000 characters

# # # # # # # # else:
# # # # # # # #     print(f"Failed to fetch bookmarks. Status code: {response.status_code}")


# # # # # # # from selenium import webdriver
# # # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # # from selenium.webdriver.common.by import By
# # # # # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # # # # import time
# # # # # # # import re

# # # # # # # # Start Chrome
# # # # # # # options = webdriver.ChromeOptions()
# # # # # # # options.add_argument("--start-maximized")

# # # # # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # # # # # Go to X login page
# # # # # # # driver.get("https://x.com/login")

# # # # # # # print("Please log in manually within 60 seconds...")
# # # # # # # time.sleep(60)  # Give you time to log in manually

# # # # # # # # Go to bookmarks page
# # # # # # # driver.get("https://x.com/i/bookmarks")
# # # # # # # time.sleep(10)  # Wait for bookmarks to load

# # # # # # # # Get page source
# # # # # # # html = driver.page_source

# # # # # # # # Find all /status/ URLs
# # # # # # # status_urls = re.findall(r'https://(?:www\.)?x\.com/[^/]+/status/\d+', html)

# # # # # # # # Remove duplicates and print
# # # # # # # unique_urls = set(status_urls)
# # # # # # # print(f"Found {len(unique_urls)} status links:")
# # # # # # # for url in unique_urls:
# # # # # # #     print(url)

# # # # # # # driver.quit()


# # # # # # import time
# # # # # # import re
# # # # # # from selenium import webdriver
# # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # from webdriver_manager.chrome import ChromeDriverManager

# # # # # # options = webdriver.ChromeOptions()
# # # # # # options.add_argument("--start-maximized")
# # # # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # # # driver.get("https://x.com/login")
# # # # # # print("Please log in manually within 60 seconds...")
# # # # # # time.sleep(60)  # login manually

# # # # # # driver.get("https://x.com/i/bookmarks")
# # # # # # time.sleep(5)

# # # # # # # Scroll down multiple times to load more bookmarks
# # # # # # scroll_pause_time = 3
# # # # # # last_height = driver.execute_script("return document.body.scrollHeight")

# # # # # # for i in range(100):  # scroll 10 times; increase if needed
# # # # # #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # # # # #     time.sleep(scroll_pause_time)
# # # # # #     new_height = driver.execute_script("return document.body.scrollHeight")
# # # # # #     if new_height == last_height:
# # # # # #         print("Reached bottom of page or no new content.")
# # # # # #         break
# # # # # #     last_height = new_height

# # # # # # # After scrolling, grab the page source
# # # # # # html = driver.page_source

# # # # # # # Extract all status URLs
# # # # # # status_urls = re.findall(r'https://(?:www\.)?x\.com/[^/]+/status/\d+', html)
# # # # # # unique_urls = set(status_urls)

# # # # # # print(f"Found {len(unique_urls)} status links:")
# # # # # # for url in unique_urls:
# # # # # #     print(url)

# # # # # # driver.quit()


# # # # # import requests
# # # # # from bs4 import BeautifulSoup

# # # # # cookies = {
# # # # #     'night_mode': '2',
# # # # #     'kdt': 'ObXU3CF1ijADzvJQZDr03t8T2QewV4v16YlFn1R8',
# # # # #     'auth_token': 'e893a19c85fd2700624e2e98d9512ec532484dff',
# # # # #     'ct0': '83e27f861fc91304666479b15910c21395988d33ddeaef2a73f42f601ccd17f555e1e55e9f8c56d81d3b8d62bae64c71a999f27e53074b340139d47dea7211b6ca50167ece6d1b9c8b57f37894fd1cd3',
# # # # #     'twid': 'u%3D1790358327974842368',
# # # # #     'personalization_id': '"v1_CUAtJ+qa8XJ0da9Imv8i+g=="',
# # # # #     'dnt': '1',
# # # # #     'des_opt_in': 'Y',
# # # # #     '_ga': 'GA1.2.1180435595.1716297519',
# # # # #     '_ga_RJGMY4G45L': 'GS1.1.1745724145.2.0.1745724403.60.0.0',
# # # # #     'ph_phc_TXdpocbGVeZVm5VJmAsHTMrCofBQu3e0kN8HGMNGTVW_posthog': '%7B%22distinct_id%22%3A%2201964709-4b2c-796e-a67f-99b9dfec9244%22%2C%22%24sesid%22%3A%5B1746364057238%2C%2201969b68-b7f4-75a3-963a-8e623d9a6a35%22%2C1746364053492%5D%7D',
# # # # #     'guest_id_ads': 'v1%3A174784399256673946',
# # # # #     'guest_id_marketing': 'v1%3A174784399256673946',
# # # # #     'guest_id': 'v1%3A174784399256673946',
# # # # #     'lang': 'en',
# # # # #     '__cf_bm': '8zVW4fmTgHQV57KC4CU.OprjyymbAy7Rw79PLA7msmk-1748668293-1.0.1.1-uW5_Vud.EjwYQBLuDNDvtgyjrFO3bvQn2zc7QWBa7JgpsQTLZxPTF2PWvK1u8W96l0CPM4prpFJtp23YUJzOlgDe6tUyGe1ZL9goiwq_hoE',
# # # # # }

# # # # # headers = {
# # # # #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# # # # #     'accept-language': 'en-US,en;q=0.9',
# # # # #     'cache-control': 'max-age=0',
# # # # #     'priority': 'u=0, i',
# # # # #     'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
# # # # #     'sec-ch-ua-mobile': '?0',
# # # # #     'sec-ch-ua-platform': '"Windows"',
# # # # #     'sec-fetch-dest': 'document',
# # # # #     'sec-fetch-mode': 'navigate',
# # # # #     'sec-fetch-site': 'same-origin',
# # # # #     'sec-fetch-user': '?1',
# # # # #     'upgrade-insecure-requests': '1',
# # # # #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
# # # # # }

# # # # # response = requests.get('https://x.com/i/bookmarks', cookies=cookies, headers=headers)

# # # # # # Check status
# # # # # if response.status_code == 200:
# # # # #     html = response.text
    
# # # # #     from bs4 import BeautifulSoup
# # # # #     soup = BeautifulSoup(html, 'html.parser')
    
# # # # #     status_links = set()
# # # # #     for a_tag in soup.find_all('a', href=True):
# # # # #         href = a_tag['href']
# # # # #         if '/status/' in href:
# # # # #             # Clean URL (strip query parameters if you want)
# # # # #             link = href.split('?')[0]
# # # # #             # Make absolute URL if relative
# # # # #             if link.startswith('/'):
# # # # #                 link = 'https://x.com' + link
# # # # #             status_links.add(link)
    
# # # # #     print(f"Found {len(status_links)} status links:")
# # # # #     for link in status_links:
# # # # #         print(link)
# # # # # else:
# # # # #     print("Failed to load bookmarks page:", response.status_code)

# # # # # print(response.url)      # Final URL after redirects
# # # # # print(response.status_code)
# # # # # # print(response.text[:1000])  # Print first 1000 chars of the HTML page


# # # # # import requests

# # # # # url = 'https://x.com/i/bookmarks'  # replace with your URL

# # # # # headers = {
# # # # #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
# # # # # }

# # # # # response = requests.get(url, headers=headers)

# # # # # if response.status_code == 200:
# # # # #     print(response.text)
# # # # # else:
# # # # #     print(f"Failed to retrieve page. Status code: {response.status_code}")


# # # # import time
# # # # from selenium import webdriver
# # # # from selenium.webdriver.chrome.service import Service
# # # # from selenium.webdriver.chrome.options import Options
# # # # from selenium.webdriver.common.by import By

# # # # # ===== CONFIG =====
# # # # CHROMEDRIVER_PATH = r"C:/Users/gayat/.wdm/drivers/chromedriver/win64/135.0.7049.42/chromedriver-win32/chromedriver.exe"
# # # # AUTH_TOKEN = "fcd9913b8b41850747a30e8c4d4cb92622330fc9"  # Replace with your auth_token
# # # # CT0_TOKEN = "61030a9d65771dae2048829a0169309ff1a70d2b27c1fc5fe242c833c16e341dc4f46ca5a455c3143e015aa0a3b397b1a3111d34ff3660808bfb22a4d0a276768d4dbb73c43b0f1ba1b2007b7c56a8eb"  # Replace with your ct0
# # # # BOOKMARKS_URL = "https://twitter.com/i/bookmarks"
# # # # OUTPUT_HTML_PATH = "twitter_bookmarks.html"

# # # # # ===== SETUP SELENIUM =====
# # # # options = Options()
# # # # # Comment out headless if you want to see the browser for debugging:
# # # # options.add_argument("--headless")
# # # # options.add_argument("--disable-blink-features=AutomationControlled")
# # # # options.add_argument("--window-size=1920,1080")

# # # # service = Service(CHROMEDRIVER_PATH)
# # # # driver = webdriver.Chrome(service=service, options=options)

# # # # try:
# # # #     # Step 1: Open twitter.com domain to set cookies
# # # #     driver.get("https://twitter.com/")
# # # #     time.sleep(3)

# # # #     # Step 2: Add cookies for authentication
# # # #     driver.add_cookie({
# # # #         "name": "auth_token",
# # # #         "value": AUTH_TOKEN,
# # # #         "domain": ".twitter.com",
# # # #         "path": "/",
# # # #         "secure": True,
# # # #         "httpOnly": True,
# # # #     })
# # # #     driver.add_cookie({
# # # #         "name": "ct0",
# # # #         "value": CT0_TOKEN,
# # # #         "domain": ".twitter.com",
# # # #         "path": "/",
# # # #         "secure": True,
# # # #         "httpOnly": False,
# # # #     })

# # # #     # Step 3: Go to bookmarks page
# # # #     driver.get(BOOKMARKS_URL)
# # # #     time.sleep(5)

# # # #     # Step 4: Scroll down repeatedly to load all bookmarks
# # # #     last_height = driver.execute_script("return document.body.scrollHeight")
# # # #     scroll_pause_time = 3
# # # #     while True:
# # # #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # # #         time.sleep(scroll_pause_time)
# # # #         new_height = driver.execute_script("return document.body.scrollHeight")
# # # #         if new_height == last_height:
# # # #             break
# # # #         last_height = new_height

# # # #     print("[✓] Finished loading all bookmarks")

# # # #     # Step 5: Save page source (full HTML)
# # # #     with open(OUTPUT_HTML_PATH, "w", encoding="utf-8") as f:
# # # #         f.write(driver.page_source)

# # # #     print(f"[✓] Saved bookmarks page HTML to {OUTPUT_HTML_PATH}")

# # # #     # === OPTIONAL: Unbookmark all bookmarks ===
# # # #     print("[*] Starting unbookmarking process...")
# # # #     total_unbookmarked = 0
# # # #     while True:
# # # #         buttons = driver.find_elements(By.XPATH, "//div[@data-testid='unbookmark']")
# # # #         if not buttons:
# # # #             # Scroll down to load more if available
# # # #             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # # #             time.sleep(3)
# # # #             buttons = driver.find_elements(By.XPATH, "//div[@data-testid='unbookmark']")
# # # #             if not buttons:
# # # #                 break

# # # #         for btn in buttons:
# # # #             try:
# # # #                 driver.execute_script("arguments[0].scrollIntoView(true);", btn)
# # # #                 btn.click()
# # # #                 total_unbookmarked += 1
# # # #                 time.sleep(1)  # delay to avoid rate limits
# # # #             except Exception as e:
# # # #                 print(f"[!] Error clicking unbookmark: {e}")

# # # #         time.sleep(2)  # let page update

# # # #     print(f"[✓] Unbookmarking finished! Total removed: {total_unbookmarked}")

# # # # finally:
# # # #     driver.quit()


# # # import time
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from selenium.webdriver.common.by import By
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # ===== CONFIG =====
# # # AUTH_TOKEN = "fcd9913b8b41850747a30e8c4d4cb92622330fc9"  # Replace with your auth_token
# # # CT0_TOKEN = "61030a9d65771dae2048829a0169309ff1a70d2b27c1fc5fe242c833c16e341dc4f46ca5a455c3143e015aa0a3b397b1a3111d34ff3660808bfb22a4d0a276768d4dbb73c43b0f1ba1b2007b7c56a8eb"  # Replace with your ct0
# # # BOOKMARKS_URL = "https://twitter.com/i/bookmarks"
# # # OUTPUT_HTML_PATH = "twitter_bookmarks.html"

# # # # ===== SETUP SELENIUM =====
# # # options = Options()
# # # # Uncomment below if you want to see the browser window:
# # # # options.add_argument("--headless")
# # # options.add_argument("--disable-blink-features=AutomationControlled")
# # # options.add_argument("--window-size=1920,1080")

# # # service = Service(ChromeDriverManager().install())
# # # driver = webdriver.Chrome(service=service, options=options)

# # # try:
# # #     # Step 1: Open twitter.com domain to set cookies
# # #     driver.get("https://twitter.com/")
# # #     time.sleep(3)

# # # # Step 2: Add cookies for authentication
# # #     driver.add_cookie({
# # #         "name": "auth_token",
# # #         "value": AUTH_TOKEN,
# # #         "domain": "twitter.com",   # no leading dot
# # #         "path": "/",
# # #         "secure": True,
# # #         "httpOnly": True,
# # #     })

# # #     driver.add_cookie({
# # #         "name": "ct0",
# # #         "value": CT0_TOKEN,
# # #         "domain": "twitter.com",   # no leading dot
# # #         "path": "/",
# # #         "secure": True,
# # #         "httpOnly": False,
# # #     })

# # #     # Step 1: Open twitter.com domain to set cookies
# # #     # driver.get("https://twitter.com/")
# # #     # time.sleep(3)

# # #     # # Step 2: Add cookies for authentication
# # #     # driver.add_cookie({
# # #     #     "name": "auth_token",
# # #     #     "value": AUTH_TOKEN,
# # #     #     "domain": ".twitter.com",
# # #     #     "path": "/",
# # #     #     "secure": True,
# # #     #     "httpOnly": True,
# # #     # })
# # #     # driver.add_cookie({
# # #     #     "name": "ct0",
# # #     #     "value": CT0_TOKEN,
# # #     #     "domain": ".twitter.com",
# # #     #     "path": "/",
# # #     #     "secure": True,
# # #     #     "httpOnly": False,
# # #     # })

# # #     # Step 3: Go to bookmarks page
# # #     driver.get(BOOKMARKS_URL)
# # #     time.sleep(5)

# # #     # Step 4: Scroll down repeatedly to load all bookmarks
# # #     last_height = driver.execute_script("return document.body.scrollHeight")
# # #     scroll_pause_time = 3
# # #     while True:
# # #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # #         time.sleep(scroll_pause_time)
# # #         new_height = driver.execute_script("return document.body.scrollHeight")
# # #         if new_height == last_height:
# # #             break
# # #         last_height = new_height

# # #     print("[✓] Finished loading all bookmarks")

# # #     # Step 5: Save page source (full HTML)
# # #     with open(OUTPUT_HTML_PATH, "w", encoding="utf-8") as f:
# # #         f.write(driver.page_source)

# # #     print(f"[✓] Saved bookmarks page HTML to {OUTPUT_HTML_PATH}")

# # #     # === OPTIONAL: Unbookmark all bookmarks ===
# # #     print("[*] Starting unbookmarking process...")
# # #     total_unbookmarked = 0
# # #     while True:
# # #         buttons = driver.find_elements(By.XPATH, "//div[@data-testid='unbookmark']")
# # #         if not buttons:
# # #             # Scroll down to load more if available
# # #             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # #             time.sleep(3)
# # #             buttons = driver.find_elements(By.XPATH, "//div[@data-testid='unbookmark']")
# # #             if not buttons:
# # #                 break

# # #         for btn in buttons:
# # #             try:
# # #                 driver.execute_script("arguments[0].scrollIntoView(true);", btn)
# # #                 btn.click()
# # #                 total_unbookmarked += 1
# # #                 time.sleep(1)  # delay to avoid rate limits
# # #             except Exception as e:
# # #                 print(f"[!] Error clicking unbookmark: {e}")

# # #         time.sleep(2)  # let page update

# # #     print(f"[✓] Unbookmarking finished! Total removed: {total_unbookmarked}")

# # # finally:
# # #     driver.quit()


# # import os
# # import json
# # import subprocess
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.options import Options

# # # === Step 1: Config file setup ===
# # config = {
# #     "extractor": {
# #         "twitter": {
# #             "cookies": {
# #                 "auth_token": "e893a19c85fd2700624e2e98d9512ec532484dff",
# #                 "ct0": "83e27f861fc91304666479b15910c21395988d33ddeaef2a73f42f601ccd17f555e1e55e9f8c56d81d3b8d62bae64c71a999f27e53074b340139d47dea7211b6ca50167ece6d1b9c8b57f37894fd1cd3"
# #             },
# #             "original": True,
# #             "retweets": False,
# #             "replies": True,
# #             "videos": True
# #         }
# #     },
# #     "downloader": {
# #         "part": False,
# #         "overwrite": False
# #     },
# #     "output": r"C:\hpswsetup\sp108788\Actress\Phoyos"
# # }

# # # Save the config to gallery-dl's config path
# # config_path = os.path.join(os.path.expanduser('~'), 'gallery-dl.conf')

# # with open(config_path, 'w') as f:
# #     json.dump(config, f, indent=4)

# # print(f"[+] Config saved to {config_path}")

# # # === Step 2: Download Twitter bookmarks using gallery-dl ===
# # gallery_dl_exe = r"C:/Users/gayat/AppData/Roaming/Python/Python311/Scripts/gallery-dl.exe"

# # try:
# #     print("[*] Starting download of your X Bookmarks...")
# #     subprocess.run([gallery_dl_exe, 'https://twitter.com/i/bookmarks'], check=True)
# #     print("[✓] Download complete!")

# #     # === Step 3: Auto-Unbookmark using Selenium ===
# #     print("[*] Starting unbookmarking process...")

# #     # Your ChromeDriver path - make sure this matches your Chrome browser version
# #     CHROMEDRIVER_PATH = r"C:/Users/gayat/.wdm/drivers/chromedriver/win64/135.0.7049.42/chromedriver-win32/chromedriver.exe"
# #     auth_token = config["extractor"]["twitter"]["cookies"]["auth_token"]
# #     ct0_token = config["extractor"]["twitter"]["cookies"]["ct0"]

# #     # Setup Chrome options
# #     options = Options()
# #     options.add_argument("--headless")  # comment out if you want to watch the browser
# #     options.add_argument("--disable-blink-features=AutomationControlled")
# #     options.add_argument("--window-size=1920,1080")

# #     service = Service(CHROMEDRIVER_PATH)
# #     driver = webdriver.Chrome(service=service, options=options)

# #     # Step A: Visit Twitter homepage to get proper domain
# #     driver.get("https://twitter.com/")
# #     time.sleep(3)  # wait for full page load

# #     print("Current URL before adding cookies:", driver.current_url)

# #     # Add cookies WITHOUT domain to avoid mismatch errors
# #     driver.add_cookie({
# #         "name": "auth_token",
# #         "value": auth_token,
# #         "path": "/",
# #         "secure": True,
# #         "httpOnly": True,
# #     })

# #     driver.add_cookie({
# #         "name": "ct0",
# #         "value": ct0_token,
# #         "path": "/",
# #         "secure": True,
# #         "httpOnly": False,
# #     })

# #     # Step B: Go to bookmarks page
# #     driver.get("https://twitter.com/i/bookmarks")
# #     time.sleep(5)  # allow bookmarks page to load

# #     # === Step C: Loop through and unbookmark all ===
# #     total_unbookmarked = 0
# #     while True:
# #         unbookmark_buttons = driver.find_elements(By.XPATH, "//div[@data-testid='unbookmark']")
# #         if not unbookmark_buttons:
# #             # Scroll to load more bookmarks and retry
# #             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #             time.sleep(3)
# #             unbookmark_buttons = driver.find_elements(By.XPATH, "//div[@data-testid='unbookmark']")
# #             if not unbookmark_buttons:
# #                 break  # no more bookmarks found, exit loop

# #         for btn in unbookmark_buttons:
# #             try:
# #                 driver.execute_script("arguments[0].scrollIntoView(true);", btn)
# #                 btn.click()
# #                 total_unbookmarked += 1
# #                 time.sleep(1)  # avoid rate limits
# #             except Exception as e:
# #                 print(f"[!] Error clicking unbookmark: {e}")

# #         time.sleep(2)  # wait a bit before next loop

# #     print(f"[✓] Unbookmarking finished! Total removed: {total_unbookmarked}")

# #     driver.quit()

# # except subprocess.CalledProcessError as e:
# #     print(f"[!] Download failed: {e}")
# # except FileNotFoundError:
# #     print(f"[!] gallery-dl executable not found at: {gallery_dl_exe}")
# # except Exception as ex:
# #     print(f"[!] Something went wrong: {ex}")


# import requests

# cookies = {
#     'night_mode': '2',
#     'kdt': 'ObXU3CF1ijADzvJQZDr03t8T2QewV4v16YlFn1R8',
#     'dnt': '1',
#     'des_opt_in': 'Y',
#     '_ga': 'GA1.2.1180435595.1716297519',
#     '_ga_RJGMY4G45L': 'GS1.1.1745724145.2.0.1745724403.60.0.0',
#     'ph_phc_TXdpocbGVeZVm5VJmAsHTMrCofBQu3e0kN8HGMNGTVW_posthog': '%7B%22distinct_id%22%3A%2201964709-4b2c-796e-a67f-99b9dfec9244%22%2C%22%24sesid%22%3A%5B1746364057238%2C%2201969b68-b7f4-75a3-963a-8e623d9a6a35%22%2C1746364053492%5D%7D',
#     'guest_id_ads': 'v1%3A174784399256673946',
#     'guest_id_marketing': 'v1%3A174784399256673946',
#     'guest_id': 'v1%3A174784399256673946',
#     'personalization_id': '"v1_xTKeoU2IBS0q3H2nLEo37g=="',
#     'g_state': '{"i_l":0}',
#     'auth_token': 'fcd9913b8b41850747a30e8c4d4cb92622330fc9',
#     'ct0': '61030a9d65771dae2048829a0169309ff1a70d2b27c1fc5fe242c833c16e341dc4f46ca5a455c3143e015aa0a3b397b1a3111d34ff3660808bfb22a4d0a276768d4dbb73c43b0f1ba1b2007b7c56a8eb',
#     'twid': 'u%3D1790358327974842368',
#     'lang': 'en',
#     '__cf_bm': 'EEwuCckdi42mBllevavNGI6u1LWJK7Na73xnYAo7nJ4-1748683155-1.0.1.1-2zT80elwusiRPNEr8d4Wlyoeb5O478Ix9MnRv3FLos2rqViYXogpkAuR1vVAq6.rAbQk3rtBaayyQliy0mII786BntNQO_XPxqKHD9Irn1I',
# }

# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'max-age=0',
#     'priority': 'u=0, i',
#     'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
#     # 'cookie': 'night_mode=2; kdt=ObXU3CF1ijADzvJQZDr03t8T2QewV4v16YlFn1R8; dnt=1; des_opt_in=Y; _ga=GA1.2.1180435595.1716297519; _ga_RJGMY4G45L=GS1.1.1745724145.2.0.1745724403.60.0.0; ph_phc_TXdpocbGVeZVm5VJmAsHTMrCofBQu3e0kN8HGMNGTVW_posthog=%7B%22distinct_id%22%3A%2201964709-4b2c-796e-a67f-99b9dfec9244%22%2C%22%24sesid%22%3A%5B1746364057238%2C%2201969b68-b7f4-75a3-963a-8e623d9a6a35%22%2C1746364053492%5D%7D; guest_id_ads=v1%3A174784399256673946; guest_id_marketing=v1%3A174784399256673946; guest_id=v1%3A174784399256673946; personalization_id="v1_xTKeoU2IBS0q3H2nLEo37g=="; g_state={"i_l":0}; auth_token=fcd9913b8b41850747a30e8c4d4cb92622330fc9; ct0=61030a9d65771dae2048829a0169309ff1a70d2b27c1fc5fe242c833c16e341dc4f46ca5a455c3143e015aa0a3b397b1a3111d34ff3660808bfb22a4d0a276768d4dbb73c43b0f1ba1b2007b7c56a8eb; twid=u%3D1790358327974842368; lang=en; __cf_bm=EEwuCckdi42mBllevavNGI6u1LWJK7Na73xnYAo7nJ4-1748683155-1.0.1.1-2zT80elwusiRPNEr8d4Wlyoeb5O478Ix9MnRv3FLos2rqViYXogpkAuR1vVAq6.rAbQk3rtBaayyQliy0mII786BntNQO_XPxqKHD9Irn1I',
# }

# response = requests.get('https://x.com/i/bookmarks', cookies=cookies, headers=headers)
# print(response.text)

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # set True to run in background
    context = browser.new_context()
    
    # You must log in manually here unless you load cookies/session
    page = context.new_page()
    page.goto("https://x.com/i/bookmarks")
    
    input("Log in to X in the browser window and press Enter here once done...")
    
    html = page.content()
    with open("bookmarks.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    browser.close()
