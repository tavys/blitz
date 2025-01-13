from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

if __name__ == "__main__":
    sample_text = "Solana is experiencing a major boom in the DeFi sector!"
    sentiment_score = analyze_sentiment(sample_text)
    print(f"Sentiment Score: {sentiment_score}")