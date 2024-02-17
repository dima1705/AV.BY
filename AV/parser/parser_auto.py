import time
import requests
from bs4 import BeautifulSoup
from parser_photo_av import photo_parser_av
from db_client import save_auto


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


auto_id = 0


def get_auto(url):

    r = requests.get(url, headers=headers)
    auto = BeautifulSoup(r.content, "html.parser")

    data = auto.find_all("div", class_="listing__items")

    time.sleep(1)

    for el in data:
        elem = el.find_all("div", class_="listing-item__wrap")
        for dat in elem:
            cart_url = 'https://cars.av.by' + dat.find("a").get("href")
            global auto_id
            auto_id += 1
            get_cart_auto(cart_url, auto_id)


def get_cart_auto(cart_url, auto_id):

    FOREIGN_KEY = 1

    r = requests.get(cart_url, headers=headers)
    auto2 = BeautifulSoup(r.content, "html.parser")

    data2 = auto2.find('div', class_='card')

    name = data2.find('h1', class_="card__title").text.replace('Продажа ', '')
    number_post = data2.find('ul', class_='card__stat').text.split('№')[-1].replace(' ', '')

    # r2 = requests.get('https://api.av.by/offers/' + number_post, headers=headers)

    price_for_bel_rub = data2.find('div', class_='card__price-primary').text.split('р.')[0]
    price_for_usd = data2.find('div', class_='card__price-secondary').text.split('$')[0]
    params = data2.find('div', class_='card__params').text.split(',')
    year = params[0]
    kpp = params[1]
    volume = params[2]
    type_engine = params[3]
    probeg = params[4]
    description = data2.find('div', class_='card__description').text.split(',')
    kyzov = description[0]
    privod = description[1]
    color = description[2]
    power = data2.find('div', class_='card__modification')
    if power is not None:
        power = power.text.replace('Все параметры','').split('.,')
    else:
        power = ''

    comment = data2.find('div', class_='card__comment-text')
    if comment is not None:
        comment = comment.text
    else:
        comment = ''

    save_auto(name, price_for_bel_rub, price_for_usd, year, kpp, volume, type_engine, probeg, kyzov, privod,
              color, power, comment, FOREIGN_KEY)
    photo_parser_av(number_post, auto_id, headers)




# get_cart_auto('https://cars.av.by/alfa-romeo/155/100647333', 1)
