import requests
from bs4 import BeautifulSoup

hp_url = "https://books.toscrape.com/index.html"
response = requests.get(hp_url)
html = response.content
scraped = BeautifulSoup(html, 'html.parser')

# scrapes all links to book titles
# > navigates to the destination page of every link
# >> scrapes the description of a book from it

# return a list of dictionaries containing:
# Title, price and description

books_info = []

articles = scraped.find_all("article",class_="product_pod")
for art in articles:
  title = art.h3.a["title"]
  price = float(art.find("p",class_="price_color").text.lstrip("£"))

  books_info.append({"Title": title ,
    "Price" : price})

print(books_info)
