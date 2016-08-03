# ClintonTrumpPostConventions
Twitter Scrape

Scrape tweets from twitter into a DB. Convert the DB to a CSV file.
Installation

    pip install -r requirements.txt

Setup

    Create a file called private.py.
    Sign up for a Twitter developer account.
    Create an application here.
    Set the following keys in private.py. You can get these values from the app you created:
        TWITTER_KEY   # this is Token
        TWITTER_SECRET # this is token_secret
        TWITTER_APP_KEY #Consumer App key
        TWITTER_APP_SECRET # consumer App secret
    Set the following key in private.py.
        CONNECTION_STRING -- use sqlite:///tweets.db as a default if you need to.

Usage

    python scraper.py to scrape. Use Ctrl + C to stop.
    python dump.py to generate tweets.csv, which contains all the tweet data that was scraped.
    If you want to edit behavior, change settings in settings.py.
