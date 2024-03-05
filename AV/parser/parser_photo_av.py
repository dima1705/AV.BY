import json
import time
import requests
from bs4 import BeautifulSoup
from db_client import save_photo


def photo_parser_av(number_auto, auto_id, headers):

    r = requests.get(f'https://api.av.by/offers/{number_auto}', headers=headers)
    photos = r.json()['photos']

    for i in photos:
        m_photo = i['medium']['url']
        save_photo(m_photo, auto_id)
