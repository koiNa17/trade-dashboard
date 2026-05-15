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

def get_trade_stats(stats_data_id):
    url = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
    params = {
        "appId": API_KEY,
        "statsDataId": stats_data_id,
        "cdArea": "50103",
        "cdTimeFrom": "2006000000",
        "cdTimeTo": "2010000000",
        "limit": 100,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    stats_data = get_trade_stats("0003228117")

    # 国の分類を確認
    total = stats_data["GET_STATS_DATA"]["STATISTICAL_DATA"]["RESULT_INF"]["TOTAL_NUMBER"]
    print(f"データ件数：{total}件")