# 📧➡️📱 Email to Telegram Bot

A Python bot that monitors your email inbox and forwards new messages to Telegram, with optional spam filtering using Google's Gemini AI.

## Features
- Fetches unread emails via IMAP
- Optional AI-powered spam filtering
- Sends clean notifications to Telegram
- Configurable check intervals

## ⚙️ Setup

### Prerequisites
- Python 3.8+
- Telegram bot token from [@BotFather](https://t.me/BotFather)
- Gmail/IMAP-enabled email account

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/email-telegram-bot.git
    cd email-telegram-bot
2. Install requirements:
    ```bash
    pip install -r requirements.txt
3. Configure environment:
    ```bash
    cp .env.example .env
    nano .env  # Edit with your credentials
4. Run the bot:
    ```bash
    python main.py

## Config (.env file)
# Required
EMAIL_ADDRESS="your@gmail.com"
EMAIL_PASSWORD="your_password"
TELEGRAM_TOKEN="123:ABC"
TELEGRAM_CHAT_ID="456789"
GOOGLE_API_KEY="AIza..."