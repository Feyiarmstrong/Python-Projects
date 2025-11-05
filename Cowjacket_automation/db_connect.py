import psycopg2
import os
from dotenv import load_dotenv
from logger import log_info, log_error

# Load environment variables from .env
load_dotenv()

def connect_to_db():
    """Connect to the PostgreSQL database and return the connection object."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        log_info("Connected to the database successfully!")
        return conn
    except Exception as e:
        log_error(f"Failed to connect to the database: {e}")
        print("Failed to connect to the database")
        return None

def check_table(conn):
    """Fetch and display sample rows from the phonerequest table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phonerequest LIMIT 5")
        rows = cursor.fetchall()
        log_info("Fetched sample data from phonerequest table.")
        print("Sample data from phonerequest table:")
        for row in rows:
            print(row)
    except Exception as e:
        log_error(f"Error fetching sample data: {e}")
        print(f"Error fetching sample data: {e}")

if __name__ == "__main__":
    connection = connect_to_db()
    if connection:
        check_table(connection)
        connection.close()
        log_info("Database connection closed.")