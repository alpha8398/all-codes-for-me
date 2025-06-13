# import requests
# from bs4 import BeautifulSoup

# url = "https://hianime.to/watch/vinland-saga-40?ep=1134"
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup.prettify())  # Print the HTML nicely formatted
# else:
#     print("Failed to retrieve the page:", response.status_code)


from selenium import webdriver

url = "https://hianime.to/watch/vinland-saga-40?ep=1134"
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
print(html)

driver.quit()
