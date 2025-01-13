import requests
from bs4 import BeautifulSoup

def fetch_tweets_by_keyword(keyword, max_results=100):
    # Example function for fetching tweets
    url = f"https://api.twitter.com/2/tweets/search/recent?query={keyword}&max_results={max_results}"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch tweets: {response.status_code}")

# Test function
if __name__ == "__main__":
    keyword = "Solana"
    print(fetch_tweets_by_keyword(keyword))