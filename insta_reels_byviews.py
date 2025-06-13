from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

USERNAME = "heyalphamale83@gmail.com"
PASSWORD = "G22@&&&&"
PROFILE_URL = f"https://www.instagram.com/dilruba16_/reels/"

def login_instagram(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(7)  # wait for login to complete

def scroll_reels_page(driver, scrolls=5):
    driver.get(PROFILE_URL)
    time.sleep(5)

    for _ in range(scrolls):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

def get_reels_data(driver):
    reels = driver.find_elements(By.CSS_SELECTOR, 'article a')
    data = []

    for reel in reels:
        href = reel.get_attribute('href')
        try:
            view_text = reel.find_element(By.CSS_SELECTOR, 'span span').text
            views = int(view_text.replace(',', '').replace(' views', '').strip())
            data.append({'url': href, 'views': views})
        except:
            continue  # Not a valid reel or missing views

    return sorted(data, key=lambda x: x['views'], reverse=True)

def main():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        login_instagram(driver, USERNAME, PASSWORD)
        scroll_reels_page(driver, scrolls=10)
        reels = get_reels_data(driver)

        for r in reels:
            print(f"{r['views']} views - {r['url']}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
