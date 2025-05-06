import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv(override=True)

def send_telegram_message(text):
    try:
        token = os.getenv("TELEGRAM_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        
        # Truncate long messages (Telegram has 4096 char limit)
        text = text[:4000] + "..." if len(text) > 4000 else text
        
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        response = requests.post(url, json={
            "chat_id": chat_id,
            "text": text,
        })
        
        if not response.ok:
            print(f"Telegram API error: {response.status_code} - {response.text}")
        return response.ok
        
    except Exception as e:
        print(f"Telegram send failed: {str(e)}")
        return False