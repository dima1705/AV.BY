import json
import time
import requests
from bs4 import BeautifulSoup
from db_client import save_photo


def photo_parser_av(number_auto, auto_id, headers):

    r = requests.get(f'https://api.av.by/offers/{number_auto}', headers=headers)
    photos = r.json()['photos']

    for i in photos:
        s_photo = i['small']['url']
        m_photo = i['medium']['url']
        b_photo = i['big']['url']

        save_photo(s_photo, m_photo, b_photo, auto_id)
