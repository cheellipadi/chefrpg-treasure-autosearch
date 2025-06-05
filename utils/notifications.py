from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()  # Loads from .env file in current directory

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_latest_response(since_update_id):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    params = {"offset": since_update_id, "timeout": 30} # Long-poll for 30s, if any response is received during this time, api will return the message
    try:
        print("getting updates")
        res = requests.get(url, params=params).json()
        print(f"update res: {res}")
        return res.get("result", [])
    except Exception as e:
        print("Polling failed:", e)
        return []

def wait_for_user_input(valid_responses=("Y", "N"), timeout=60*60*2): # 2 hour timeout by default
    start_time = time.time()
    last_update_id = None

    while time.time() - start_time < timeout:
        updates = get_latest_response(last_update_id + 1 if last_update_id else None)

        for update in updates:
            last_update_id = update["update_id"]
            if "message" in update and str(update["message"]["chat"]["id"]) == TELEGRAM_CHAT_ID and update["message"]["date"] > start_time:
                msg = update["message"]["text"].strip().upper()
                if msg in valid_responses:
                   
                    return msg
                else:
                    send_telegram_message(f"You have provided an invalid response")
            # Start next long-poll (30s) immediately

    return None

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


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    print(f"sending message to: {url}")
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to send message: {e}")