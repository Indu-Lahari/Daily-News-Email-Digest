import requests

api_key = "b79705e5c12f417cbcff102e5ee27af2"

url = ("https://newsapi.org/v2/everything?q=apple&from=2024-07-09&to=2024-07-09&sortBy=popularity&apiKey=b79705e5c12f417cbcff102e5ee27af2")

# Make requests
r = requests.get(url)

# r.text is changed to r.json() to get data as dict not as str
content = r.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
