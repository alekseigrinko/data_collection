import os
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def get_request():
    url = "https://api.spoonacular.com/recipes/complexSearch"

    query = choose_query()
    params = {"apiKey": os.getenv("API_KEY"), "query": query, "number": 10}

    response = requests.get(url, params=params)
    print(response.ok)

    j_dats = response.json()

    for place in j_dats.get('results'):
        print(place.get('title'))
        print(place.get('image'))
        print("---")


def choose_query():
    categories = ["Pasta", "Pizza", "Soup", "Meat"]

    print("Выберите категорию рецепта:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    choice = input("Введите номер желаемой категории: ")

    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        return categories[int(choice) - 1]
    else:
        print("Ошибка выбора. Попробуйте еще раз")
        return choose_query()


if __name__ == "__main__":
    get_request()
    #подготовил первое задание
