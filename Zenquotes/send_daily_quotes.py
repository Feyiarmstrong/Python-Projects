from logger_module import log_info, log_error
from db_setup import get_active_users
from fetch_quote import fetch_quote
from send_email import send_quote_email


def send_daily_quotes():
    """Fetch a quote and send it to all active users."""
    quote = fetch_quote()
    if not quote:
        log_error("No quote fetched today!")
        return

    users = get_active_users()
    if not users:
        log_info("No active users to send emails to.")
        return

    for name, email in users:
        try:
            send_quote_email(email, name, quote)
            log_info(f"Email sent to {email}")
        except Exception as e:
            log_error(f"Failed to send email to {email}: {e}")

if __name__ == "__main__":
    send_daily_quotes()