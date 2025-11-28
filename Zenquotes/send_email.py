import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_quote_email(to_email, name, quote):
    """Send a motivational quote via Gmail SMTP using SSL (port 465)."""
    from_email = os.getenv("ddb_email") 
    password = os.getenv("ddb_password")

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Daily Launchpad Motivation By Feyisayo 🌞"
    msg.attach(MIMEText(f"Hi {name},\n\n\"{quote}\"\n\nStay Refreshed,\nFeyiarmstrong Team", 'plain'))

    try:
        # Connect using SSL
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")