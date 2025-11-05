import psycopg2

def get_connection():

    """Connect to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="mindfuel_db",
            user="postgres",   
            password="postgres",
            port="5433"
        )

        print("Database connected successfully!")
        return conn
    
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None


if __name__ == "__main__":
    get_connection()




def create_users_table():

    """Create the users table if it doesn't exist."""

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

if __name__ == "__main__":
    create_users_table()





def add_multiple_users(users):
    """Insert multiple users into the users table."""
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


if __name__ == "__main__":
    users = [
        ("Feyisayo Amstrong", "solapeajiboye@gmail.com", True, "daily"),
        ("Faruk Sedik", "faruksedik@gmail.com", True, "weekly"),
        ("Yussuf Alade", "aladeyussuf.kofo@gmail.com", True, "daily"),
        ("Ufuoma Ejite", "ufuoma.ejite@gmail.com", True, "daily"),
        ("Susan Amgbare", "susantamunokubie@gmail.com", True, "daily"),
        ("Najeeb Sulaiman", "beejan003@gmail.com", True, "daily"),
        ("Mohammed Abubakar", "ammedabubakard500@gmail.com", True, "daily"),
        ("Ganiu Odeyinka", "omowalefst@gmail.com", True, "daily"),
        ("Adebola Adesoyin", "adeboladesoyin@gmail.com", True, "daily"),
        ("Ayooluwa Jesuniyi", "jesuniyig@gmail.com", True, "daily"),
        ("Olukayode Olusegun", "olukayodeoluseguno@gmail.com", True, "daily"),
        ("Okoli Ogechukwu", "okoliogechi74@gmail.com", True, "daily"),
        ("Joshua Akintayo", "akinspajo@gmail.com", True, "daily"),
        ("Kabir Olawale", "kabirolawalemohammed@gmail.com", True, "daily"),
        ("Kate Chisom", "katechisom072@gmail.com", True, "daily")
    ]

    add_multiple_users(users)



def get_active_users():
    """Fetch all active users from the database."""
    conn = get_connection()  # make sure this function exists in db.py
    if not conn:
        return []

    try:
        cur = conn.cursor()
        cur.execute("SELECT name, email FROM users WHERE is_active = TRUE;")
        users = cur.fetchall()
        return users
    except Exception as e:
        print(f"Failed to fetch users: {e}")
        return []
    finally:
        cur.close()
        conn.close()
