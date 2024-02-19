import requests

# Your Dev.to API key
api_key = 'npWUegKufgTMzqERFRZaos68'

# Read the article content from the Markdown file
with open('devto_article.md', 'r') as file:
    article_content = file.read()

# Article data
article_data = {
    'article': {
        'title': 'Automating Article Publishing to Dev.to with Python',
        'body_markdown': article_content,
        'tags': ['python', 'devto', 'automation'],  # Add appropriate tags
        'published': True  # Set to True to publish the article immediately
    }
}

# API endpoint for creating an article
create_article_url = 'https://dev.to/api/articles'

# Headers including API key
headers = {
    'api-key': api_key,
    'content-type': 'application/json'
}

# Send POST request to create the article
response = requests.post(create_article_url, json=article_data, headers=headers)

# Check if the request was successful
if response.status_code == 201:
    print("Article published successfully!")
    article_url = response.json().get('url')
    print("Article URL:", article_url)
else:
    print("Failed to publish the article. Status code:", response.status_code)
