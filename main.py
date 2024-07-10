import requests

api_key = "b79705e5c12f417cbcff102e5ee27af2"

url = ("https://newsapi.org/v2/everything?q=apple&from=2024-07-09&to=2024-07-09&sortBy=popularity&apiKey=b79705e5c12f417cbcff102e5ee27af2")

r = requests.get(url)
content = r.text
print(content)