import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ESTAT_API_KEY")

def get_trade_data():
    url = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsList"
    params = {
        "appId": API_KEY,
        "searchWord": "貿易統計",
        "limit": 5,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    data = get_trade_data()
    print(data)