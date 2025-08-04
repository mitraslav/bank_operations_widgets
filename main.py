
from dotenv import load_dotenv
import os
import requests

url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=20"
load_dotenv()
api_key = os.getenv("API_KEY")

payload = {}
headers = {
    "apikey": api_key
}
response = requests.get(url, headers=headers, data=payload)

print(response.text)

