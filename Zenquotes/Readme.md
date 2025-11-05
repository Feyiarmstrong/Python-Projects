MindFuel Automated Daily Quote Email Platform

## **Project Overview**

This project is a **production-ready backend service** built for MindFuel, a mental wellness startup. It automates sending motivational quotes to subscribed users every day while logging activity and providing an admin summary.  

Key features:  

- Fetches daily motivational quotes from the "https://zenquotes.io/api/random"

- Sends personalized emails to active users

- Logs all events and errors in daily log files

- Sends a daily summary email to admin  

- Can be scaled for hundreds or thousands of users  

---

## **Tech Stack**

- **Python 3.13**  

- **PostgreSQL** for storing user data  

- **SendGrid** for email delivery (SMTP alternative supported)  

- **Task Scheduler (Windows)** for automation  

- **Libraries used:** `requests`, `psycopg2`, `logging`, `os`  

---

## **Project Structure**

```
Zenquotes/

│

├─ db_setup.py                # Database connection and setup

├─ test.py                    # Functions to manage users and queries

├─ fetch_quote.py             # Fetches quotes from ZenQuotes API

├─ send_email.py              # Sends quote emails to users

├─ send_daily_quotes.py       # Main script to send daily quotes with logging

├─ admin_summary.py           # Sends daily summary log to admin

├─ logger_module.py           # Logging setup and log utilities

├─ requirements.txt           # Python dependencies


```


---

## **Database Setup**

1. Create a PostgreSQL database called `mindfuel` (or your preferred name).  

2. Create a `users` table with the following structure:


```sql

CREATE TABLE IF NOT EXISTS users (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(150) UNIQUE NOT NULL,

    is_active BOOLEAN DEFAULT TRUE,

    frequency VARCHAR(20) DEFAULT 'daily',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
```


3. Insert users with active subscriptions:


```sql

INSERT INTO users (name, email, is_active, frequency) 

VALUES 

('Stella Armstrong', 'stella@example.com', TRUE, 'daily'),

('David Dan', 'david@example.com', TRUE, 'daily');

```


---

## **Installation & Setup**

### **1. Clone the repository**

```bash

git clone <repo-url>

cd Zenquotes

```


### **2. Create and activate a virtual environment**

```bash

python -m venv venv

# On Git Bash or WSL

source venv/Scripts/activate


# On Windows CMD

venv\Scripts\activate

```


### **3. Install dependencies**

```bash

pip install -r requirements.txt

```


**Dependencies include:**  

- `requests` – for API calls  

- `psycopg2` – PostgreSQL integration  

- `sendgrid` – email delivery (optional if using SendGrid)  

- `logging` – built-in, no install required  

---



## **Configuration**

1. **Database connection**  

Update `db_setup.py` with your PostgreSQL credentials:


```python

conn = psycopg2.connect(

    host="localhost",

    dbname="mindfuel",

    user="your_username",

    password="your_password",

    port=5432

)

```

2. **SendGrid / SMTP**  

- For Gmail SMTP:

  - Generate an **App Password** under Google Account → Security → App Passwords  
  
  - Add it to `send_email.py`  

- For SendGrid API:

  - Create an account at [SendGrid](https://sendgrid.com/)  

  - Add API key to your environment variables (`SENDGRID_API_KEY`)  

---


## **Running the Scripts**


### **1. Send Daily Quotes**

```bash

python send_daily_quotes.py

```

- Fetches a quote from ZenQuotes API  

- Sends it to all **active users**  

- Logs success and failures in `logs/quote_email_YYYY-MM-DD.log`  


### **2. Send Admin Summary**

```bash

python send_admin_summary.py

```

- Reads the daily log file  

- Summarizes total emails sent and failures  

- Sends a summary email to admin  

---



## **Logging**

- Logs are stored in the `logs/` folder  

- Daily log files are named `quote_email_YYYY-MM-DD.log`  

- Each log entry format:


```

2025-10-30 07:00:00 | INFO | Email sent to stella@example.com

2025-10-30 07:00:05 | ERROR | Failed to send email to david@example.com

```

- `logger_module.py` provides utility functions:

  - `log_info(message)` – for successful events  

  - `log_error(message)` – for errors  

  - `read_today_log()` – reads today’s log file  

  - `get_log_stats()` – returns total emails sent and errors  

---


## **Automating with Task Scheduler (Windows)**

1. Open **Task Scheduler**  

2. Click **Create Basic Task…**  

3. Set **Name**: `Daily Quote Emails`  

4. Trigger: **Daily at 7:00 AM**  

5. Action: **Start a Program**  

   - Program: Path to Python executable in your venv  

   - Arguments: `"C:\path	o\Zenquotes\send_daily_quotes.py"`  

6. Repeat to schedule `send_admin_summary.py` a few minutes later  

---



## **Project Flow**

1. `send_daily_quotes.py` runs:  

   - Fetch quote → Send emails → Log results  

2. `logger_module.py` tracks all actions  

3. `admin_summary.py` runs:  

   - Reads log → Compiles stats → Sends admin summary  

---


## **Optional Enhancements**

- HTML formatting for admin summary email  

- Retry mechanism for failed user emails  

- Weekly or monthly reports for admin  

- Dockerize the app for cloud deployment  


---

## **Outcome**

- Fully automated **motivational email system**  

- **Scalable** for hundreds/thousands of users  

- **Logs** ensure transparency and track errors  

- Admin receives a **daily report**  