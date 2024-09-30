# https://books.toscrape.com/
# извлечь информацию о всех книгах на сайте во всех категориях: название, цену,
# количество товара в наличии (In stock (19 available)) в формате integer, описание

import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://books.toscrape.com/"
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

session = requests.session()

all_books = []


def get_book_info(book_info: dict, link: str):
    r_stock = session.get(link, headers=headers)
    soup = BeautifulSoup(r_stock.text, "html.parser")
    # description = list(soup.findChildren())
    book_info['description'] = find_description(list(soup.findChildren()))
    stock_info = soup.find_all('tr')
    for info in stock_info:
        if info.find('th').getText() == 'Availability':
            book_info['availability'] = info.find('td').getText()
            return book_info


def find_description(info: list):
    for i in range(len(info)):
        if info[i].getText() == 'Product Description':
            return info[i + 1].getText()


def f():
    page_f = 1
    p_url = f"catalogue/page-{page_f}.html"
    while True:
        response = session.get(url + p_url, headers=headers)
        if not response.ok or page_f > 3:  # задается количество обрабатываемых страниц
            break
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all('li', {'class': 'col-xs-6'})

        for book in books:
            book_info = {}
            book_info['name'] = book.find('h3').getText()
            book_info['product_price'] = float(book.find('p', {'class': 'price_color'}).getText()[2:])
            book_link = url + 'catalogue/' + book.find('div', {'class': 'image_container'}).find('a').get('href')
            book_info['book_link'] = book_link # добавил ссылку на книгу
            book_info = get_book_info(book_info, book_link)

            all_books.append(book_info)

        print(f"Обработана {page_f} страница")
        page_f += 1

    pprint(all_books)
    pprint(len(all_books))


if __name__ == '__main__':
    f()
