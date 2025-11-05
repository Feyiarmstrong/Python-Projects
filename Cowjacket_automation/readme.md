# Jira Service Desk Automation & Supabase Integration

This project demonstrates end-to-end automation of **Jira Service Desk** using Python, combined with **Supabase PostgreSQL** integration. It enables creating, fetching, and managing service requests dynamically, both directly via scripts and automatically from a Supabase database. This showcases skills in **Python automation, API integration, database management, and cloud-based workflow automation**.

---

## Features

- **Automated Jira request creation**: Dynamically create Jira Service Desk requests with custom summaries and descriptions.

- **Fetch and view requests**: Retrieve latest tickets with key details, including status.

- **Supabase integration**: Automatically generate Jira tickets from new entries in Supabase `phonerequest` table.

- **Clickable terminal links**: Open Jira requests directly from the terminal.

- **Email notifications**: Jira automatically notifies users of new requests.

- **Environment-based configuration**: Secure handling of credentials for both Jira and Supabase using a `.env` file.

---

## Tools & Technologies

- **Python 3.x** – Core scripting language

- **Jira API / Jira Service Desk API** – Manage Jira tickets programmatically

- **Supabase PostgreSQL** – Cloud-hosted database for automated requests

- **psycopg2** – Python library to connect to PostgreSQL

- **Python-dotenv** – Environment variable management

- **Requests** – HTTP requests for API calls

---

## Project Structure

```

CowJacket_automation/

├── db_connect.py           # Handles PostgreSQL DB connection

├── fetch_request.py        # Optional, fetches Jira requests

├── jira_integration.py     # Handles Jira API connection & creating tickets

├── logger.py               # Logging setup

├── main.py                 # Main workflow: fetch DB requests & create Jira tickets

├── .env                    # Environment variables (DB & Jira credentials)

├── logs/                   # Folder where automation.log will be created

└── venv/                   # virtual environment (optional, add to .gitignore)

```

---

## Environment Setup

1. Install dependencies:

```bash
pip install jira requests python-dotenv psycopg2
```

2. Create a `.env` file in the project root:

```
# Supabase / PostgreSQL
DB_HOST=your_supabase_host
DB_PORT=your_port
DB_NAME=postgres
DB_USER=your_user
DB_PASSWORD=your_password

# Jira
JIRA_EMAIL=your_email@example.com
JIRA_TOKEN=your_api_token
JIRA_BASE_URL=https://yourdomain.atlassian.net
JIRA_PROJECT_KEY=YOUR_PROJECT_KEY
```

> Ensure no spaces around `=`. Keep API tokens and database passwords secure.

---

## Usage

### Task 1 & 2: Jira Automation

#### Create a Jira Request

```bash
python jira_integration.py
```

- Creates a request in Jira Service Desk.
- Prints a clickable link to open the request in the browser.

Example output:

```
Request created successfully!
Issue Key: COW-3
Summary: Sparkle Alert: New Request from Python
Open Request -> [clickable terminal link]
```

#### Fetch Latest Requests

```bash
python fetch_request.py
```

- Retrieves recent Jira requests.
- Shows **Issue Key, Summary, Status**, and **clickable link**.

Example output:

```
COW-2 | Sparkle Alert: New Request from Python | Status: To Do | Open Request
COW-1 | Test Request from Python | Status: To Do | Open Request
```

---

### Task 3: Supabase → Jira Automation

- Automatically reads new entries from `phonerequest` table in Supabase.
- Maps form fields to Jira request fields.
- Creates tickets in Jira Service Desk within 15 minutes of submission.
- Attaches form data to the Jira ticket when available.
- Logs all key events and errors for monitoring.

#### Run Automation Script

```bash
python supabase_to_jira.py
```

- Script fetches new phone requests and creates Jira tickets.
- Automatically handles mapping of request fields, including summary and description.
- Ensures no duplicates by checking previous requests.

---

## Key Achievements

- Integrated Python automation with both **cloud database** (Supabase) and **Jira Service Desk**.
- Implemented real-time request generation from database to Jira.
- Enabled clickable links in terminal for quick access to tickets.
- Used environment variables for secure credential management.
- Implemented error handling and logging to track failures in automation pipeline.

---

## Challenges & Solutions

- **Authentication errors**: Verified Jira API token and Supabase credentials.
- **Service Desk & request type mismatch**: Dynamically fetched Service Desk ID and request type IDs from Jira API.
- **Database mapping**: Carefully mapped Supabase form fields to Jira request fields to ensure accurate ticket creation.
- **Logging & monitoring**: Built logging mechanism to record successes and failures for automation reliability.

---

## Outcome

- Fully functional automation pipeline from **Supabase → Jira Service Desk**.
- End-to-end demonstration of **Python scripting, API integration, cloud database usage, and real-world workflow automation**.
- Portfolio-ready project showcasing strong technical skills in **Data Engineering, Python Automation, and DevOps-style pipelines**.