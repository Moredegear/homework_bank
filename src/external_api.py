import requests
import os
from dotenv import load_dotenv
import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

load_dotenv()
API_KEY = os.getenv("API_KEY")


def conversion(amount: float, code: str) -> float:
    """функция конвертации валют в рубли через запрос API"""
    logger.debug("создаем параметры API-запроса")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": amount, "from": "RUB", "to": code}
    headers = {"apikey": API_KEY}
    logger.debug("делаем запрос, получаем конвертируемую в рубли сумму и возвращаем её")
    response = requests.get(url, headers=headers, params=payload)
    result = response.json()
    amount = result
    return amount
