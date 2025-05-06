import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def is_spam(email_text):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        prompt = f"""
        Determine whether the following email content is spam or not spam. 
        Respond with 'Spam' or 'Not Spam' only.

        Email Content:
        {email_text}
        """
        response = model.generate_content(prompt)
        result = response.text.strip().lower()
        return result == 'spam'
    except Exception as e:
        print(f"Error during spam detection: {e}")
        return False
