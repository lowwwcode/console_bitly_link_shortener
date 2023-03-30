import os
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv

load_dotenv()


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        data=f'{{"long_url": "{url}"}}')
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token: str, bitlink):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    params = (
        ('unit', 'day'),
        ('units', '-1'),
    )
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}/clicks/summary',
                            headers=headers,
                            params=params)
    response.raise_for_status()
    return response.json()


def is_bitlink(token, bitlink):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    params = (
        ('unit', 'day'),
        ('units', '-1'),
    )
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}/clicks/summary',
                            headers=headers,
                            params=params)
    if response.ok:
        return True
    return False


if __name__ == '__main__':
    bitly_token = os.getenv('BITLY_TOKEN')
    user_input = input('Введите ссылку для укорачивания в формате - "https://google.com": ')
    parsed_url = urlparse(user_input)

    if is_bitlink(bitly_token, parsed_url):
        try:
            print(f'Всего кликов: {count_clicks(bitly_token, parsed_url)["total_clicks"]}')
        except requests.exceptions.HTTPError:
            print('Этот битлинк не зарегистрирован в системе, или вы ввели некорректный адрес ссылки.')
    else:
        try:
            print(f'Битлинк, {shorten_link(bitly_token, user_input)}')
        except requests.exceptions.HTTPError:
            print('Вы ввели некорректный формат ссылки или такого адреса не существует, '
                  'ссылка должна начинаться с "https://"')



 # https://bit.ly/3KfSRZY