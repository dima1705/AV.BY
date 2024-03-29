import time

import requests
from bs4 import BeautifulSoup

from AV.orm_main import ORM

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def auto_pars(number_post):
    time.sleep(1)

    r = requests.get(f'https://api.av.by/offers/{number_post}', headers=headers)
    auto = r.json()

    brand = ''
    model = ''
    engine_capacity = ''
    engine_type = ''
    transmission_type = ''
    generation_with_years = ''
    body_type = ''
    drive_type = ''
    color = ''
    mileage_km = ''

    for auto_params in auto['properties']:
        if auto_params['name'] == "brand":
            brand = auto_params['value']

        if auto_params['name'] == "model":
            model = auto_params['value']

        if auto_params['name'] == "engine_capacity":
            engine_capacity = float(auto_params['value'])

        if auto_params['name'] == "engine_type":
            engine_type = auto_params['value']

        if engine_type == 'электро':
            if auto_params['name'] == "engine_endurance":
                engine_capacity = float(auto_params['value'])

        if auto_params['name'] == "transmission_type":
            transmission_type = auto_params['value']

        if auto_params['name'] == "generation_with_years":
            generation_with_years = auto_params['value']

        if auto_params['name'] == "body_type":
            body_type = auto_params['value']

        if auto_params['name'] == "drive_type":
            drive_type = auto_params['value']

        if auto_params['name'] == "color":
            color = auto_params['value']

        if auto_params['name'] == "mileage_km":
            mileage_km = int(auto_params['value'])

    price_amount_usd = int(auto['price']["usd"]['amount'])
    price_amount_byn = int(auto['price']['byn']['amount'])
    description = ''
    for auto_d in auto:
        if auto_d == "description":
            description = auto['description']
            break
    main_photo = 'нет фото'
    if len(auto["photos"]) > 0:
        main_photo = auto["photos"][0]['medium']['url']
    location = auto["locationName"]
    brand_slag = auto['metadata']['brandSlug']
    model_slug = auto['metadata']['modelSlug']
    year = int(auto['metadata']['year'])

    r = requests.get(
        f'https://cars.av.by/{brand_slag}/{model_slug}/{number_post}',
        headers=headers
    )
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all('div', class_='card__modification')

    power = 0
    fuel_consumption = 0

    if data:
        for el in data:
            params = el.text.replace('Все параметры', '').split('.,')
            try:
                if len(params) > 1:
                    power = int(params[0].replace('л.с', ''))
                    fuel_consumption = float(
                        params[1]
                        .replace('расход', '')
                        .replace('л', '')
                        .replace(',', '.')
                    )
                elif len(params) == 1:
                    power = int(params[0].replace('л.с.', ''))
            except Exception:
                break

            else:
                break
    else:
        power = power
        fuel_consumption = fuel_consumption

    ORM.insert_brand_model_gen(brand, model, generation_with_years)

    ORM.insert_auto_parser(
        brand, model, generation_with_years, year, engine_capacity, engine_type, transmission_type,
        body_type, drive_type, color, mileage_km, power, fuel_consumption,
        price_amount_usd, price_amount_byn, description,
        main_photo, location,
    )

    if len(auto["photos"]) > 0:
        for i in auto["photos"]:
            photo = i['medium']['url']
            ORM.insert_photo(photo)
    else:
        photo = 'нет фото'
        ORM.insert_photo(photo)