from db_connect import connect_to_db
from jira_integration import JiraConnector
from logger import log_info, log_error

# ---------- Configuration ----------
MAX_REQUESTS = 10  # Number of requests to process at once
REQUEST_TYPE_NAME = "Submit a request or incident"

# ---------- Step 1: Connect to DB ----------
connection = connect_to_db()
if not connection:
    log_error("Exiting workflow: could not connect to the database.")
    exit(1)
log_info("Database connection established successfully.")

# ---------- Step 2: Connect to Jira ----------
jira = JiraConnector()
jira.connect()
if not jira.service_desk_id:
    log_error("Exiting workflow: could not connect to Jira Service Desk.")
    connection.close()
    exit(1)
log_info("Jira connection established successfully.")

# ---------- Step 3: Fetch unprocessed requests ----------
try:
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT id, name, email, description
        FROM phonerequest
        WHERE processed = FALSE
        ORDER BY created_at ASC
        LIMIT {MAX_REQUESTS};
    """)
    requests = cursor.fetchall()

    if not requests:
        log_info("No unprocessed requests found.")
        print("No new requests found.")
    else:
        log_info(f"Fetched {len(requests)} unprocessed request(s) from database.")
except Exception as e:
    log_error(f"Failed to fetch requests from DB: {e}")
    print(f"Failed to fetch requests from DB: {e}")
    connection.close()
    exit(1)

# ---------- Step 4: Create Jira tickets ----------
for req in requests:
    req_id, name, email, description = req
    try:
        jira.create_request(name, description, REQUEST_TYPE_NAME)
        log_info(f"Request ID {req_id} processed and sent to Jira successfully.")
    except Exception as e:
        log_error(f"Failed to create Jira ticket for request ID {req_id}: {e}")

# ---------- Step 5: Close DB connection ----------
connection.close()
log_info("Database connection closed.")