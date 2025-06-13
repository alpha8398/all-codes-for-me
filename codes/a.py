from selenium import webdriver

url="https://pin.it/4ZWSEJRyV"
driver = webdriver.Chrome()  
driver.get(url)


print(driver.page_source)

driver.quit()

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.pornpics.com/galleries/busty-chick-mia-callista-is-relieved-of-her-jeans-before-her-guy-fucks-her-19876670/"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, "html.parser")
#     print(soup.prettify()) 
# else:
#     print("Failed to retrieve the webpage:", response.status_code)
