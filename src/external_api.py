import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def conversion(amount, code):
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": "amount", "from": "RUB", "to": code}
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers, params=payload)
    result = response.json()
    amount = result
    return amount
