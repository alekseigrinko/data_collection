from pymongo import MongoClient
from data_collection.task2 import f
import json

client = MongoClient('localhost', 27017)
db = client['mydatabase']

books = db.books


def create_db():
    books.insert_many(f())


def find_by_name(name: str):
    return list(books.find({'name': name}))


def print_db(books: list):
    for book in books:
        for element in book:
            print(f'>>> {element}: {book[element]}')


if __name__ == '__main__':
    create_db() # заполняет базу данных
    print_db(find_by_name('Libertarianism for Beginners')) # поиск и вывод в консоль информации из базы данных


