from src.scrapers.social_media_scraper import fetch_tweets_by_keyword
from src.analysis.trend_analysis import calculate_trend_score
from src.visualizations.trend_visualizer import plot_trend_scores
from src.utils.data_cleaning import clean_data
from src.utils.logger import log_info
from src.scrapers.blockchain_scraper import fetch_trending_tokens
from solana.rpc.api import Client
import requests
import time
import json
import pandas as pd

# Define constants
PUMPFUN_API_URL = "https://api.pumpfun.io/v1/new-tokens"
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
FETCH_LIMIT = 10


def fetch_new_token_deploys():
    """
    Fetch the latest token deployments from Pumpfun API.
    """
    log_info("Fetching new token deployments from Pumpfun API...")
    try:
        response = requests.get(PUMPFUN_API_URL)
        if response.status_code == 200:
            token_data = response.json()
            log_info(f"Fetched {len(token_data)} new tokens.")
            return token_data
        else:
            log_info(f"Failed to fetch tokens: {response.status_code}")
            return []
    except Exception as e:
        log_info(f"Error fetching tokens: {e}")
        return []


def fetch_sol_transactions(token_address):
    """
    Fetch recent transactions for a specific token on Solana.
    """
    log_info(f"Fetching transactions for token: {token_address}")
    client = Client(SOLANA_RPC_URL)
    try:
        result = client.get_signatures_for_address(token_address, limit=FETCH_LIMIT)
        transactions = result.get('result', [])
        log_info(f"Fetched {len(transactions)} transactions for {token_address}.")
        return transactions
    except Exception as e:
        log_info(f"Error fetching transactions: {e}")
        return []


def save_data_to_file(data, filename):
    """
    Save processed data to a JSON file for further analysis.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        log_info(f"Data saved to {filename}.")
    except Exception as e:
        log_info(f"Error saving data to file: {e}")


def load_data_from_file(filename):
    """
    Load data from a JSON file.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        log_info(f"Data loaded from {filename}.")
        return data
    except Exception as e:
        log_info(f"Error loading data from file: {e}")
        return []


def analyze_token_engagement(tokens):
    """
    Analyze token engagement based on mentions and blockchain activity.
    """
    log_info("Analyzing token engagement...")
    analyzed_data = []
    for token in tokens:
        token_address = token.get("address")
        transactions = fetch_sol_transactions(token_address)
        engagement_score = len(transactions) * 10  # Example calculation
        analyzed_data.append({
            "name": token.get("name"),
            "address": token_address,
            "engagement_score": engagement_score,
        })
        log_info(f"Token {token['name']} has engagement score {engagement_score}.")
    return analyzed_data


def generate_token_report(tokens):
    """
    Generate a report summarizing token data.
    """
    log_info("Generating token report...")
    report = pd.DataFrame(tokens)
    report_filename = "token_report.csv"
    report.to_csv(report_filename, index=False)
    log_info(f"Token report saved to {report_filename}.")


def schedule_fetch_and_analysis(interval=3600):
    """
    Schedule periodic fetching and analysis of new token data.
    """
    log_info("Starting scheduled token analysis...")
    while True:
        log_info("Scheduled task started.")
        new_tokens = fetch_new_token_deploys()
        engagement_data = analyze_token_engagement(new_tokens)
        save_data_to_file(engagement_data, "engagement_data.json")
        generate_token_report(engagement_data)
        log_info("Scheduled task complete. Waiting for next interval...")
        time.sleep(interval)


def main():
    # Fetch new token deployments from Pumpfun
    print("Fetching new token deployments...")
    new_tokens = fetch_new_token_deploys()

    # Analyze token engagement using Solana RPC data
    print("Analyzing token engagement...")
    engagement_data = analyze_token_engagement(new_tokens)

    # Save engagement data to file
    save_data_to_file(engagement_data, "engagement_data.json")

    # Generate token report
    generate_token_report(engagement_data)

    # Example data for trend analysis
    print("Analyzing trending token narratives...")
    narrative_data = [
        {
            "topic": token["name"],
            "mentions": len(fetch_sol_transactions(token["address"])),
            "engagement": token["engagement_score"]
        }
        for token in engagement_data
    ]
    trend_data = calculate_trend_score(narrative_data)

    # Visualize token narrative trends
    print("Visualizing trending token narratives...")
    plot_trend_scores(trend_data)

    # Log completion
    log_info("Token analysis and visualization complete.")


if __name__ == "__main__":
    main()
