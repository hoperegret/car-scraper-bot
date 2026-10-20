import os
import requests
from bs4 import BeautifulSoup

# Securely grab the secrets from GitHub
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': text})

def scrape_cars():
    # Example logic: you can add your specific OLX/Apify code here later
    # For now, we will send a test message to prove the cloud automation works
    send_telegram_message("🚗 Hourly Check: The cloud bot is running successfully!")

if __name__ == "__main__":
    print("Running scraper on GitHub Cloud...")
    scrape_cars()
