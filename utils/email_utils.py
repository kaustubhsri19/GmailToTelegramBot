import imaplib
import email
from email.header import decode_header
import os
import logging
from dotenv import load_dotenv

load_dotenv(override=True)

def fetch_unread_emails():
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        imap.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        imap.select("inbox")
        
        _, messages = imap.search(None, '(UNSEEN)')
        email_ids = messages[0].split()
        
        if not email_ids:
            return []

        # Only fetch the latest unread email
        latest_email_id = email_ids[-1]

        _, data = imap.fetch(latest_email_id, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        subject = decode_header(msg["Subject"])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode("utf-8", errors="ignore")

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain" and not part.get("Content-Disposition"):
                    body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

        # ✅ Mark as seen
        imap.store(latest_email_id, '+FLAGS', '\\Seen')

        return [{
            "from": msg.get("From"),
            "subject": subject,
            "body": body
        }]

    except Exception as e:
        logging.error(f"IMAP error: {str(e)}")
        return []
    finally:
        try:
            imap.logout()
        except:
            pass
