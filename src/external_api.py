import os

import requests
from dotenv import load_dotenv


def get_amount(transaction: dict) -> float | None:
    """Выводит сумму транзакции в рублях
    Если валюта не является RUB, выводит конвертируемую сумму в рублях"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    try:
        if currency == "RUB":
            return float(amount)

        else:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            load_dotenv()
            api_key = os.getenv("API_KEY")

            if not api_key:
                raise ValueError("API_KEY not found in environment variables")

            headers = {"apikey": api_key}

            response = requests.get("GET", url, headers=headers)
            result = response.json()

            return float(result["result"])

    except KeyError as e:
        raise Exception(f"Missing required field in transaction: {str(e)}")

    except ValueError as e:
        raise Exception(f"Invalid value format: {str(e)}")
