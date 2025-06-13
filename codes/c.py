x = """

https://i.pinimg.com/736x/cd/d9/6e/cdd96e6c3c2dde756410597b5f5c3542.jpg
"""

# Split the string into individual URLs
urls = x.strip().split("\n")

# Format each URL into the desired <img> tag format
formatted = '\n'.join([f'<img src="{url}" href="{url}">' for url in urls])

print(formatted)
