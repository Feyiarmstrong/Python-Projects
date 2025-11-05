from send_email import send_quote_email
from logger_module import read_today_log, get_log_stats
from fetch_quote import fetch_quote

ADMIN_EMAIL = "solapeajiboye@gmail.com"
ADMIN_NAME = "Feyisayo Armstrong"

def send_admin_summary():
    """Send daily log summary with stats to admin."""
    sent, failed = get_log_stats()
    log_content = read_today_log()
    quote = fetch_quote()

    summary = f"""
    <h3>MindFuel Daily Summary</h3>
    <p><strong>Quote Sent:</strong> "{quote}"</p>
    <p><strong>Emails Sent:</strong> {sent}</p>
    <p><strong>Failed Deliveries:</strong> {failed}</p>
    <hr>
    <pre>{log_content}</pre>
    """

    send_quote_email(
        to_email=ADMIN_EMAIL,
        name=ADMIN_NAME,
        quote=summary
    )

if __name__ == "__main__":
    send_admin_summary()