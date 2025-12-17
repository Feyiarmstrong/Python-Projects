import os
import time
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection(max_retries=2, retry_delay=2):
    """
    Connect to the PostgreSQL database with retry logic
    (useful for Docker startup delays).
    """
    retries = 0

    while retries < max_retries:
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT"),
            )
            print("Database connected successfully!")
            return conn

        except psycopg2.OperationalError as e:
            retries += 1
            print(f"Connection failed ({retries}/{max_retries}): {e}")

            if retries < max_retries:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Giving up.")
                raise

        except Exception as e:
            print(f"Unexpected error: {e}")
            return None


def create_users_table():
    """
    Create the users table if it does not exist.
    """
    conn = get_connection()
    if not conn:
        return

    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE NOT NULL,
                is_active BOOLEAN DEFAULT TRUE,
                frequency VARCHAR(20) DEFAULT 'daily',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        print("Users table created successfully.")

    except Exception as e:
        print(f"Failed to create users table: {e}")

    finally:
        cur.close()
        conn.close()


def add_multiple_users(users):
    """
    Insert multiple users into the users table.
    """
    conn = get_connection()
    if not conn:
        return

    try:
        cur = conn.cursor()
        cur.executemany("""
            INSERT INTO users (name, email, is_active, frequency)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (email) DO NOTHING;
        """, users)
        conn.commit()
        print(f"{len(users)} users added successfully.")

    except Exception as e:
        print(f"Failed to add users: {e}")

    finally:
        cur.close()
        conn.close()


def get_active_users():
    """
    Fetch all active users.
    """
    conn = get_connection()
    if not conn:
        return []

    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT name, email FROM users WHERE is_active = TRUE;"
        )
        return cur.fetchall()

    except Exception as e:
        print(f"Failed to fetch users: {e}")
        return []

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_users_table()

    users = [
        ("Engr Feyisayo", "solapeajiboye@gmail.com", True, "daily"),
        ("Feyi Armstrong", "feyiarmstrong@gmail.com", True, "weekly"),
        ("Lady Kash", "kashopefoluwaarmstrong@gmail.com", True, "daily"),
        ("Engr Faruk", "faruksedik@yahoo.com", True, "daily")
    ]

    add_multiple_users(users)

    active_users = get_active_users()
    print("Active users:", active_users)