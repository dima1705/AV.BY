import json
import time
import requests
from bs4 import BeautifulSoup
import psycopg2
from parser_auto import get_auto
# from headers import headers
from db_client import save_brand, save_model, save_generation


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

brand_id = 0
model_id = 0


def auto_with_mileage(brand_id):

    r = requests.get('https://cars.av.by/', headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all('li', class_='catalog__item')

                                    ### Марка

    for brand in data:
        mark = brand.find("span", class_="catalog__title").text.replace(' ', '-')
        brand_id += 1
        print(f'Марка: {mark}')

        save_brand(mark)
        get_model_and_generation(mark, brand_id)


def get_model_and_generation(mark, brand_id):

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

        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content, "html.parser")
        data2 = soup.find_all('label', class_='dropdown__card-button')

        save_model(model, brand_id)
        get_auto(url)

        print(f'Модель: {model} ------ {brand_id}')

        time.sleep(1)

        ##### Поколение
        global model_id
        model_id += 1
        for i in data2:

            generation = i.find('span', class_='dropdown__card-text').text

            save_generation(generation, model_id)
            print(f'Поколение: {generation} ------ {model_id}')


auto_with_mileage(brand_id)

