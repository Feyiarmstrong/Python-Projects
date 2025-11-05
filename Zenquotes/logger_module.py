import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Log file path with date
log_file = os.path.join("logs", f"quote_email_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_info(message):
    logging.info(message)
    print(message)

def log_error(message):
    logging.error(message)
    print(message)


def read_today_log():
    """Return the content of today's log file."""
    try:
        with open(log_file, "r") as f:
            return f.read()
    except Exception as e:
        return f"Failed to read log: {e}"
    


def get_log_stats():
    """Summarize today's log file: emails sent and errors."""
    try:
        with open(log_file, "r") as f:
            logs = f.readlines()

        sent_count = sum("Email sent to" in line for line in logs)
        error_count = sum("ERROR" in line for line in logs)

        return {
            "emails_sent": sent_count,
            "errors": error_count
        }

    except Exception as e:
        return {
            "emails_sent": 0,
            "errors": 0,
            "error": str(e)
        }