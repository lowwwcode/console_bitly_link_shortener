import os

import requests
from dotenv import load_dotenv

load_dotenv()

BITLY_TOKEN = os.getenv('BITLY_TOKEN')

headers = {
    'Authorization': f'Bearer {BITLY_TOKEN}',
    'Content-Type': 'application/json',
}

response = requests.get('https://api-ssl.bitly.com/v4/user', headers=headers)
response.raise_for_status()

print(response.json())
