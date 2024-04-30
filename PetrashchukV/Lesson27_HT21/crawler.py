from requests import get
from bs4 import BeautifulSoup
import json


def extract_pagination_links(soup):
    pagination_section = soup.find('section', class_="pagination")
    if pagination_section:
        pagination_links = pagination_section.find_all('a')
        return [link.get('href') for link in pagination_links]
    else:
        return []


def return_links(product_link):
    response = get(product_link)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find('section', class_="results-products")
    links = items.find_all('div', class_="ph-new-catalog-tovar-title")
    list_of_links = ['https://pethouse.ua' + link.find('a').attrs['href'] for link in links]
    return list_of_links


base_url = 'https://pethouse.ua/ua/shop/sobakam/suhoi-korm/page/'
for index in range(1, 6):
    url = base_url + str(index)
    pagination_links = extract_pagination_links(BeautifulSoup(get(url).content, "html.parser"))
    list_of_links = return_links(url)
    print('Links for Page', index)
    print("\n".join(list_of_links))
    with open(f'suhoi-korm_page_{index}.json', 'w') as writer:
        json.dump(list_of_links, writer, indent=4)


print('Pagination Links for Page', index)
print(pagination_links)

'''
page_number = 1

while True:
    url = base_url + str(page_number)
    response = get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    pagination_links = extract_pagination_links(soup)
    items = soup.find('section', class_="results-products")
    links = items.find_all('div', class_="ph-new-catalog-tovar-title")
    print('PAGE', page_number)
    list_of_links = ['https://pethouse.ua' + link.find('a').attrs['href'] for link in links]
    print("\n".join(list_of_links))
    print("Pagination Links for Next Page:")
    print(pagination_links)
    if not pagination_links:
        break
    page_number += 1
'''