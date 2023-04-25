import os
import argparse
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    """Примет на вход ссылку, и auth токен, вернет короткую ссылку bitlink"""
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        json={'long_url': url})
    response.raise_for_status()
    return response.json()['link']


def get_clicks_count(token: str, url):
    """Принимает ссылку bitlink и auth токен. Вернет количество кликов по этому битлинку."""
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
    """Вернет True если ссылка является битлинком, и False если не является битлинком."""
    parsed_url = urlparse(url)

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}',
                            headers=headers)
    return response.ok


if __name__ == '__main__':

    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')

    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="Link to shorten or bitlink", type=str)
    args_link = parser.parse_args()

    if is_bitlink(bitly_token, args_link.link):
        try:
            print(f'Всего кликов: {get_clicks_count(bitly_token, args_link.link)}')
        except requests.exceptions.HTTPError:
            print('Этот битлинк не зарегистрирован в системе, или вы ввели некорректный адрес ссылки.')
    else:
        try:
            print(f'Битлинк, {shorten_link(bitly_token, args_link.link)}')
        except requests.exceptions.HTTPError:
            print('Вы ввели некорректный формат ссылки или такого адреса не существует, '
                  'ссылка должна начинаться с "https://"')
