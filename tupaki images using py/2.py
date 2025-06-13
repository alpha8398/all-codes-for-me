from bs4 import BeautifulSoup

# Replace 'yourfile.html' with the path to your HTML file
with open('tupaki_search_results.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all <a> tags
a_tags = soup.find_all('a')

# Print each tag, its href attribute, and its text
for tag in a_tags:
    print("Tag:", tag)
    print("Href:", tag.get('href'))
    print("Text:", tag.text.strip())
    print()
