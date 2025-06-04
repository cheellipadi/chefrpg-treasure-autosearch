from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Loads from .env file in current directory

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_photo(image_path, caption=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    print(f"sending photo to: {url}")
    with open(image_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': TELEGRAM_CHAT_ID, 'caption': caption}
        try:
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
        except Exception as e:
            print(f"Failed to send image: {e}")