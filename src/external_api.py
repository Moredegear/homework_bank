import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def conversion(amount,cod):
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": "1200", "from": "RUB", "to": cod}
    headers = {"apikey":API_KEY}
    response = requests.get(url, headers=headers, params=payload)
    result = response.json()
    amount = result['result']
    return amount

