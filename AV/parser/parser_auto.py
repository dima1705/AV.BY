import time
import requests
from bs4 import BeautifulSoup
from AV.parser.auto import auto_pars


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_auto(url):

    r = requests.get(url, headers=headers)
    auto = BeautifulSoup(r.content, "html.parser")

    data = auto.find_all("div", class_="listing__items")

    time.sleep(1)

    for el in data:
        elem = el.find_all("div", class_="listing-item__wrap")
        for dat in elem:
            card_url = 'https://cars.av.by' + dat.find("a").get("href")
            number_post = card_url.split('/')[-1]

            auto_pars(number_post)