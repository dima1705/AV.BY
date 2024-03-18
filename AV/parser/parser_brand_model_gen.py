import time
import requests
from bs4 import BeautifulSoup
from AV.parser.parser_auto import get_auto

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def auto_with_mileage():

    r = requests.get('https://cars.av.by/', headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all('li', class_='catalog__item')

                                    ### Марка

    for brand in data:
        mark = brand.find("span", class_="catalog__title").text.replace(' ', '-')
        print(f'Проход по марке: {mark}')

        get_model_and_generation(mark)


def get_model_and_generation(mark):

    r = requests.get(f'https://cars.av.by/{mark}', headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    data = soup.find_all('li', class_='catalog__item')

    time.sleep(2)

                                    ##### Модель

    for el in data:
        time.sleep(1)
        model = el.find("span", class_="catalog__title").text.lower().replace(' ', '-').replace('(', '').replace(
            ')', '')

        url = f'https://cars.av.by/{mark}/{model}'

        print(f'Проход по модели: {model}')

        get_auto(url)


