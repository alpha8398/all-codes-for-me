
import os
import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def parse_cookies_txt(file_path):
    cookies = []
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 7:
                cookie = {
                    "domain": parts[0],
                    "path": parts[2],
                    "secure": parts[3].upper() == "TRUE",
                    "expiry": int(parts[4]),
                    "name": parts[5],
                    "value": parts[6],
                }
                cookies.append(cookie)
    return cookies

def download_media_from_x_post(post_url, cookie_txt_path, output_folder="downloads"):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://x.com")
    time.sleep(5)

    cookies = parse_cookies_txt(cookie_txt_path)
    for cookie in cookies:
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"⚠️ Skipping cookie {cookie['name']} - {e}")

    driver.get(post_url)
    print(f"🔍 Visiting post: {post_url}")
    time.sleep(10)

    os.makedirs(output_folder, exist_ok=True)
    count = 0

    # ✅ Download images
    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        src = img.get_attribute("src")
        if src and "twimg.com/media" in src:
            src = re.sub(r"name=\w+", "name=orig", src)
            try:
                img_data = requests.get(src).content
                filename = os.path.join(output_folder, f"image_{count}.jpg")
                with open(filename, "wb") as f:
                    f.write(img_data)
                print(f"✅ Downloaded Image: {filename}")
                count += 1
            except Exception as e:
                print(f"❌ Error downloading image: {e}")

    # ✅ Download videos or GIFs
    video_tags = driver.find_elements(By.TAG_NAME, "video")
    for video in video_tags:
        src = video.get_attribute("src")
        if src:
            try:
                vid_data = requests.get(src).content
                ext = "mp4" if ".mp4" in src else "bin"
                filename = os.path.join(output_folder, f"video_{count}.{ext}")
                with open(filename, "wb") as f:
                    f.write(vid_data)
                print(f"✅ Downloaded Video: {filename}")
                count += 1
            except Exception as e:
                print(f"❌ Error downloading video: {e}")

    if count == 0:
        print("⚠️ No media found. The tweet may be private, deleted, or cookies expired.")
    else:
        print(f"🎉 Downloaded {count} media file(s).")

    input("Press Enter to close browser...")
    driver.quit()

# 👇 Call the function
download_media_from_x_post(
    post_url="https://x.com/ASMT07070708/status/1874542085015265677",
    cookie_txt_path=r"C:\hpswsetup\sp108788/codes/all_cookies.txt"
)