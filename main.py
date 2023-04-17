import os
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json={'long_url': url})
    response.raise_for_status()
    return response.json()['link']


def get_count_clicks(token: str, url):
    parsed_url = urlparse(url)
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = (
        ('unit', 'day'),
        ('units', '-1'),
    )
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}/clicks/summary',
                            headers=headers,
                            params=params)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(token, url):
    parsed_url = urlparse(url)
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}',
                            headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    user_input = input('Введите ссылку для укорачивания в формате - "https://google.com": ')

    if is_bitlink(bitly_token, user_input):
        try:
            print(f'Всего кликов: {get_count_clicks(bitly_token, user_input)}')
        except requests.exceptions.HTTPError:
            print('Этот битлинк не зарегистрирован в системе, или вы ввели некорректный адрес ссылки.')
    else:
        try:
            print(f'Битлинк, {shorten_link(bitly_token, user_input)}')
        except requests.exceptions.HTTPError:
            print('Вы ввели некорректный формат ссылки или такого адреса не существует, '
                  'ссылка должна начинаться с "https://"')



 # https://bit.ly/3KfSRZY