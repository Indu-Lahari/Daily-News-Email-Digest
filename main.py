import requests
from send_mail import news_digest

api_key = "b79705e5c12f417cbcff102e5ee27af2"

url = ("https://newsapi.org/v2/everything?q=apple&from=2024-07-09&to=2024-07-09&sortBy=popularity&apiKey=b79705e5c12f417cbcff102e5ee27af2&language=en")

# Make requests
r = requests.get(url)

# r.text is changed to r.json() to get data as dict not as str
content = r.json()

news = ""
# Access the article titles and descriptions
for article in content["articles"]:
    if article["title"] is not None:
        news = news + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

news = news.encode("UTF-8")
news_digest(news)