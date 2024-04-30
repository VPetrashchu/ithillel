from requests import get
from bs4 import BeautifulSoup
import json

def return_parameters(link):
    response = get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    rating = soup.find('div', class_="list-rating-img").text.strip()
    price = soup.find('span', class_="ph-new-catalog-price-block-oldprice").text.strip()
    return {'link': link, 'rating': rating, 'price': price}

list_of_result = []

with open('suhoi-korm.json') as reader:
    list_of_links = json.load(reader)
    for link in list_of_links:
        list_of_result.append(return_parameters(link))

with open('pethouse_downloaded_result.json', 'w', encoding='utf-8') as writer:
    json.dump(list_of_result, writer, indent=4, ensure_ascii=False)

