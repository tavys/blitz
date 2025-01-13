import matplotlib.pyplot as plt

def plot_trend_scores(trends):
    plt.figure(figsize=(10, 6))
    plt.bar(trends['topic'], trends['trend_score'], color='blue')
    plt.xlabel('Topics')
    plt.ylabel('Trend Score')
    plt.title('Trending Topics in Solana Ecosystem')
    plt.show()

# Test plot
if __name__ == "__main__":
    sample_trends = {
        'topic': ['NFTs', 'DeFi', 'GameFi'],
        'trend_score': [250, 180, 320]
    }
    plot_trend_scores(sample_trends)