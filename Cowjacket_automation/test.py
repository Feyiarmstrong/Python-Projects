from db_connect import connect_to_db

def check_rows():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM phonerequest")
        count = cursor.fetchone()[0]
        print(f"Total rows in phonerequest: {count}")
        cursor.close()
        conn.close()
    else:
        print("Failed to connect to database.")

if __name__ == "__main__":
    check_rows()