import requests

BASE_URL = "https://api.solana.com"


def fetch_recent_transactions():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getRecentBlockhash"
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch recent transactions")

if __name__ == "__main__":
    print(fetch_recent_transactions())