# README.md

## Project
**Blitz – Jobfinder for Creatives (Reimagined as a Narrative Explorer on Solana).**

## Description
The original Blitz project aimed to simplify the job search process for creative professionals like designers, architects, and photographers by aggregating job offers from various platforms, filtering them, and sending instant notifications. The name "Blitz," meaning "lightning" in German, reflects the project's commitment to speed and efficiency. 

In its new incarnation, Blitz shifts its focus to the blockchain space, specifically Solana and the Pumpfun ecosystem, to find and analyze emerging token narratives. The project leverages AI to provide real-time insights into memecoin trends, enabling users to identify lucrative opportunities instantly. By combining data from Solana's blockchain with AI-driven analysis, Blitz is now a powerful tool for traders and enthusiasts seeking to stay ahead in the volatile world of memecoins.

---

## Key Features

1. **Real-Time Narrative Tracking:**
   - Aggregates memecoin and narrative trends from Pumpfun.
   - Identifies emerging themes by analyzing blockchain data and social media trends.

2. **AI-Powered Insights:**
   - Uses AI algorithms to analyze token engagement, sentiment, and narrative growth.
   - Provides actionable insights to users through intuitive visualizations.

3. **Blockchain Integration:**
   - Fetches real-time transaction data from Solana RPC.
   - Tracks token deployments and activity for detailed analysis.

4. **Automated Reporting:**
   - Generates CSV reports and JSON summaries for advanced users.
   - Provides options for periodic updates via scheduled tasks.

5. **Custom Notifications:**
   - Sends insights directly to users' devices for instant action.

---

## Directory Structure

```plaintext
solana-trading-trends/
├── data/
│   ├── raw/
│   │   ├── social_media_data.json  # Raw data scraped from Twitter and other platforms.
│   │   ├── blockchain_transactions.json  # Raw transaction data from Solana.
│   ├── processed/
│   │   ├── trends_cleaned.csv  # Cleaned and preprocessed trend data.
│   │   ├── narrative_scores.json  # Narrative scores based on AI analysis.
├── src/
│   ├── scrapers/
│   │   ├── social_media_scraper.py  # Extracts trending keywords and hashtags.
│   │   ├── blockchain_scraper.py  # Fetches transaction data from Solana.
│   │   ├── pumpfun_data_collector.py  # Collects data specific to Pumpfun.
│   ├── analysis/
│   │   ├── trend_analysis.py  # Identifies trending narratives and calculates scores.
│   │   ├── sentiment_analysis.py  # Performs sentiment analysis on collected data.
│   │   ├── narrative_analysis.py  # Analyzes narrative growth and influence.
│   ├── visualizations/
│   │   ├── trend_visualizer.py  # Visualizes trends with graphs and charts.
│   │   ├── narrative_comparison.py  # Compares narratives using radar and bar charts.
│   ├── utils/
│       ├── data_cleaning.py  # Functions for cleaning raw data.
│       ├── config_loader.py  # Loads configuration files and environment variables.
│       ├── logger.py  # Logs events and errors for debugging.
├── tests/
│   ├── scrapers/
│   │   ├── test_social_media_scraper.py  # Unit tests for social media scraper.
│   │   ├── test_blockchain_scraper.py  # Unit tests for blockchain scraper.
│   ├── analysis/
│       ├── test_trend_analysis.py  # Unit tests for trend analysis functions.
│       ├── test_sentiment_analysis.py  # Unit tests for sentiment analysis.
├── config/
│   ├── api_keys.json  # Stores API keys for external services.
│   ├── db_config.json  # Configuration for database connections.
├── docs/
│   ├── user_guide.md  # Comprehensive user guide for the app.
│   ├── contributing.md  # Guidelines for contributors.
│   ├── architecture_diagram.png  # Diagram showing system architecture.
├── .env.example  # Example environment variable configuration.
├── requirements.txt  # Python dependencies for the project.
├── setup.py  # Setup script for packaging and installation.
├── main.py  # Entry point of the application.
├── README.md  # This document.
├── LICENSE  # Licensing information.
```

---

## Detailed File Explanations

### **`data/`**
- Contains all raw and processed data for the application.
  - `raw/`: Raw data fetched from APIs and Solana RPC.
  - `processed/`: Cleaned and structured data for analysis and reporting.

### **`src/`**
- Core logic of the project, organized into functional modules.
  - `scrapers/`: Scripts to fetch data from various sources.
  - `analysis/`: Modules for analyzing data and calculating trends.
  - `visualizations/`: Tools for creating graphs and visual summaries.
  - `utils/`: Helper functions for tasks like logging and configuration.

### **`tests/`**
- Unit and integration tests to ensure code quality and reliability.

### **`config/`**
- Configuration files for APIs and other integrations.

### **Key Scripts:**

#### `main.py`
- The central entry point of the application. Fetches data, processes it, and generates insights.

#### `social_media_scraper.py`
- Fetches trending topics, hashtags, and narratives from platforms like Twitter.

#### `blockchain_scraper.py`
- Extracts transaction data and token details from Solana.

#### `trend_analysis.py`
- Analyzes trends and calculates scores based on engagement and mentions.

#### `trend_visualizer.py`
- Creates visual representations of the analyzed trends.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/solana-trading-trends.git
   ```

2. Navigate to the project directory:
   ```bash
   cd solana-trading-trends
   ```

3. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Configure environment variables in `.env` file:
   ```plaintext
   TWITTER_API_KEY=your_twitter_api_key
   SOLANA_RPC_URL=https://api.mainnet-beta.solana.com
   ```

---

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Explore generated insights in the `data/processed/` folder and visualizations in the terminal.

3. Schedule periodic analysis with:
   ```bash
   python -c "from main import schedule_fetch_and_analysis; schedule_fetch_and_analysis()"
   ```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

We welcome contributions! Please see the `docs/contributing.md` file for guidelines.

---

## Future Enhancements

1. **Mobile App Integration:**
   - Deliver insights and notifications via a dedicated app.

2. **Deeper AI Integration:**
   - Use advanced NLP models to analyze sentiment in narratives.

3. **Customizable Dashboards:**
   - Enable users to create personalized dashboards with relevant metrics.

4. **Enhanced Visualization:**
   - Incorporate real-time, interactive charts.

---

Let us know your feedback or any features you'd like to see in future updates!
