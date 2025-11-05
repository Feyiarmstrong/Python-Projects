import logging
import os

os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/automation.log",  # Log file path
    level=logging.INFO,              # Record INFO and above (INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Timestamp, level, message
)

# Helper functions for cleaner code
def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)