import requests
import time
import pprint
from bs4 import BeautifulSoup

# Initialize empty list to store URLs
all_urls = []

# Fetch page 1
url = "https://discoversjds.com/property-search/?keyword&location=any&status=any&type=any&bedrooms=any&bathrooms=any&min-price=any&max-price=any&min-area&max-area"
filename = "page1.html"
response = requests.get(url)
with open(f"fetched/Discover/{filename}", "r") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    filtered_articles = soup.find_all('article', class_='property-item')

    urls = []
    for article in filtered_articles:
        url = article.find('a')['href']
        urls.append(url)

    all_urls.extend(urls)
    #time.sleep(3)

# Fetch pages 2 to 20
for i in range(2, 21):
    url = f"https://discoversjds.com/property-search/page/{i}/?keyword&location=any&status=any&type=any&bedrooms=any&bathrooms=any&min-price=any&max-price=any&min-area&max-area"
    filename = f"page{i}.html"
    response = requests.get(url)
    with open(f"fetched/Discover/{filename}", "r") as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
        filtered_articles = soup.find_all('article', class_='property-item')

        urls = []
        for article in filtered_articles:
            url = article.find('a')['href']
            urls.append(url)

        all_urls.extend(urls)
        #time.sleep(3)

pprint.pprint(all_urls)
count = len(all_urls)
print(f"Total URLs: {count}")
