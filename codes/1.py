import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181"

# Send a request to the URL and get the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Print the entire HTML content
    print(soup.prettify())  # prettify() formats the HTML for easier reading
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# import requests
# from bs4 import BeautifulSoup

# # URL of the blocked page
# url = "https://www.nudeindians.net/indian-model-boobs-porn-photos/" # Replace with the actual URL

# try:
#     # Make a request to the URL
#     response = requests.get(url)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Extract relevant information
#         headline = soup.find('h1', {'data-translate': 'block_headline'}).text.strip()
#         subheadline = soup.find('h2', class_='cf-subheadline').text.strip()
#         reason = soup.find('p', {'data-translate': 'blocked_why_detail'}).text.strip()
#         resolution = soup.find('p', {'data-translate': 'blocked_resolve_detail'}).text.strip()
#         ray_id = soup.find('strong', class_='font-semibold').text.strip()

#         # Print extracted information
#         print(f"Headline: {headline}")
#         print(f"Subheadline: {subheadline}")
#         print(f"Reason: {reason}")
#         print(f"Resolution: {resolution}")
#         print(f"Cloudflare Ray ID: {ray_id}")

#     else:
#         print(f"Failed to access the page. Status code: {response.status_code}")

# except Exception as e:
#     print(f"An error occurred: {e}")

# from selenium import webdriver

# url = "https://www.nudeindians.net/indian-model-boobs-porn-photos/"  # Replace with the actual URL
# driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed
# driver.get(url)

# # Wait for the page to load and print the source
# print(driver.page_source)

# driver.quit()
