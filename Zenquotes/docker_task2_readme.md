
# Task 2: Multi-Container Setup With Docker Compose

## Overview

Multi-container application for the MindFuel quote delivery service using Docker Compose. The system fetches daily motivational quotes and emails them to subscribers.

## Architecture

Services:

- mindfuel-quotes: Python application (fetches quotes, sends emails)

- mindfuel-db: PostgreSQL database (stores user data)

## Project Structure

Zenquotes/

├── compose.yml

├── Dockerfile

├── .env.docker

├── .dockerignore

├── requirements.txt

├── main.py

├── db_setup.py

├── fetch_quote.py

├── send_email.py

├── logger_module.py

└── logs/

## Quick Start

### 1. Setup Environment Variables

Edit .env.docker with your credentials:

DB_HOST

DB_NAME

DB_USER

DB_PASSWORD

DB_PORT

ddb_email=your-email@gmail.com

ddb_password=your-app-password

### 2. Build and Start

docker compose up -d --build

### 3. Initialize Database

docker compose exec mindfuel-quotes python db_setup.py

### 4. Run Application

docker compose exec mindfuel-quotes python main.py

## Common Commands

Start/Stop:

docker compose up -d              # Start services

docker compose down               # Stop services

docker compose down -v            # Stop and remove volumes

Logs:

docker compose logs -f            # View all logs

docker compose logs -f mindfuel-quotes  # View app logs

Database:

# View users

docker compose exec mindfuel-db psql -U postgres -d mindfuel_db -c "SELECT * FROM users;"

# Access database shell

docker compose exec mindfuel-db psql -U postgres -d mindfuel_db

## Verification

Test that everything works:

# 1. Check containers are running

docker compose ps

# 2. Verify database data

docker compose exec mindfuel-db psql -U postgres -d mindfuel_db -c "SELECT * FROM users;"

# 3. Send emails

docker compose exec mindfuel-quotes python main.py

## Key Features

Multi-container orchestration with Docker Compose  

Persistent database storage with volumes  

Health checks for service dependencies  

Environment-based configuration  

Isolated container networking

## Task Requirements Met

-  Multiple services defined (app + db)

-  Ports mapped for external access

-  Volumes for data persistence

-  Environment variables via .env.docker

-  Service dependencies with depends_on

-  App connects to database automatically

-  Easy rebuild with docker compose up –build

-  Quotes fetched and emails delivered successfully

## Troubleshooting

Container won’t start:

docker compose logs mindfuel-quotes

Database connection fails:

docker compose restart mindfuel-db

Table doesn’t exist:

docker compose exec mindfuel-quotes python db_setup.py

Clean restart:

docker compose down -v

docker compose up -d --build
