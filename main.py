import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

BITLY_TOKEN = os.getenv('BITLY_TOKEN')

headers = {
    'Authorization': f'Bearer {BITLY_TOKEN}',
    'Content-Type': 'application/json',
}
user_input_long_url = input('Введите ссылку для укорачивания в формате - https://google.com: ')
data = f'{{"long_url": "{user_input_long_url}"}}'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
response.raise_for_status()

print(response.json()['link'])
# print(data)