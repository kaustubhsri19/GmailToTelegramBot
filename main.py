from dotenv import load_dotenv
from utils.email_utils import fetch_unread_emails
from utils.spam_filter import is_spam
from services.telegram_bot import send_telegram_message
import time
import logging

load_dotenv(override=True)
logging.basicConfig(level=logging.INFO)

def main():
    while True:
        try:
            logging.info("Checking for new emails...")
            emails = fetch_unread_emails()
            
            if not emails:
                logging.info("No new emails found")
            else:
                logging.info(f"Found {len(emails)} new emails")
                
            for email in emails:
                content = (
                    f"📧 <b>New Email</b>\n"
                    f"From: {email['from']}\n"
                    f"Subject: {email['subject']}\n\n"
                    f"{email['body'][:1000]}"  # Truncate long emails
                )
                
                if not is_spam(email['body']):
                    if send_telegram_message(content):
                        logging.info("Email forwarded to Telegram")
                    else:
                        logging.warning("Failed to send Telegram message")
                else:
                    logging.info("Skipped spam email")
                    
        except Exception as e:
            logging.error(f"Main loop error: {str(e)}")
            
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()