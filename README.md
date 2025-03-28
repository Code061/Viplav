# Viplav Twitter Bot

Viplav is a Twitter bot that automatically tweets "Good Morning" and "Good Night" messages, responds to mentions with sentiment analysis of the tweets, and provides a friendly interaction on Twitter.

## Features

- Automatically tweets "Good Morning" and "Good Night" messages at scheduled intervals.
- Listens for mentions and responds with sentiment analysis of the mentioned tweets.
- Utilizes the Twitter API for posting tweets and managing interactions.

## Project Structure

```
Viplav
├── src
│   ├── viplav_Bot.py          # Main entry point for the Twitter bot
│   ├── utils
│   │   └── sentiment_analysis.py # Functions for analyzing tweet sentiment
│   ├── services
│   │   └── twitter_api.py      # Handles Twitter API interactions
│   └── config
│       └── settings.py         # Configuration settings for the bot
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables for sensitive information
└── README.md                   # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Viplav
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Twitter API keys and tokens:
   ```
   TWITTER_API_KEY=<your_api_key>
   TWITTER_API_SECRET=<your_api_secret>
   TWITTER_ACCESS_TOKEN=<your_access_token>
   TWITTER_ACCESS_TOKEN_SECRET=<your_access_token_secret>
   ```

4. Run the bot:
   ```
   python src/viplav_Bot.py
   ```

## Usage

- The bot will automatically tweet "Good Morning" at 8 AM and "Good Night" at 10 PM.
- When mentioned in a tweet, the bot will analyze the sentiment of the tweet and respond accordingly.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.