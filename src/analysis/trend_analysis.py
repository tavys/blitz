import pandas as pd
import numpy as np


def calculate_trend_score(data):
    # Placeholder function to calculate trend scores based on data
    data['trend_score'] = data['mentions'] * np.log1p(data['engagement'])
    return data.sort_values(by='trend_score', ascending=False)

# Test code
if __name__ == "__main__":
    sample_data = pd.DataFrame({
        'topic': ['NFTs', 'DeFi', 'GameFi'],
        'mentions': [200, 150, 300],
        'engagement': [1000, 800, 1200]
    })
    print(calculate_trend_score(sample_data))