# Task 2: Docker Compose Commands Reference

## Initial Setup

### Navigate to Project Directory
cd ~/Desktop/Python\ task/Zenquotes

### Clean Up Old Containers (First Time Only)
docker compose down
docker rm -f mindfuel-db

## Building and Starting

### Build and Start All Services
# Build images and start in detached mode
docker compose up -d --build

# Build and start with logs visible
docker compose up --build

### Start Existing Services (No Rebuild)
docker compose up -d

## Database Operations

### Initialize Database
# Create users table and add subscribers
docker compose exec mindfuel-quotes python db_setup.py

### Verify Database Data
# Check users in database
docker compose exec mindfuel-db psql -U postgres -d mindfuel_db -c "SELECT * FROM users;"

# Access PostgreSQL shell
docker compose exec mindfuel-db psql -U postgres -d mindfuel_db

### Database Queries
-- Inside PostgreSQL shell:

-- View all users
SELECT * FROM users;

-- View only active users
SELECT * FROM users WHERE is_active = TRUE;

-- Count users
SELECT COUNT(*) FROM users;

-- Exit shell
\q

## Running the Application

### Send Quotes to Users
docker compose exec mindfuel-quotes python main.py

### Run Database Setup Script
docker compose exec mindfuel-quotes python db_setup.py

### Access App Container Shell
docker compose exec mindfuel-quotes /bin/bash

## Viewing Status and Logs

### Check Container Status
# List running containers with status
docker compose ps

# View resource usage
docker compose stats

### View Logs
# All services logs (follow mode)
docker compose logs -f

# Specific service logs
docker compose logs -f mindfuel-quotes

docker compose logs -f mindfuel-db

# View last 50 lines
docker compose logs --tail=50

# Logs without following
docker compose logs

## Managing Services

### Stop Services
# Stop all services (keeps data)
docker compose down

# Stop and remove volumes (fresh start)
docker compose down -v

### Restart Services
# Restart all services
docker compose restart

# Restart specific service
docker compose restart mindfuel-quotes

docker compose restart mindfuel-db

### Stop Specific Service
docker compose stop mindfuel-quotes

docker compose stop mindfuel-db

### Start Specific Service
docker compose start mindfuel-quotes

docker compose start mindfuel-db

## Rebuilding

### Rebuild Specific Service
# Rebuild only the app
docker compose build mindfuel-quotes

# Rebuild and restart
docker compose up -d --build mindfuel-quotes

### Force Rebuild Everything
docker compose build --no-cache

docker compose up -d

## Troubleshooting Commands

### View Container Details
# Inspect container
docker inspect mindfuel-quotes

docker inspect mindfuel-db

# Check container processes
docker compose top

### Network Information
# List networks
docker network ls

# Inspect network
docker network inspect zenquotes_mindfuel-network

### Volume Information
# List volumes
docker volume ls

# Inspect database volume
docker volume inspect zenquotes_postgres_data

### Execute Commands in Container
# Run any Python script
docker compose exec mindfuel-quotes python your_script.py

# Check Python version
docker compose exec mindfuel-quotes python --version

# List files in container
docker compose exec mindfuel-quotes ls -la

## Verification Commands (For Screenshots)

### Show Multi-Service Startup
# Best for screenshot - shows both services running
docker compose ps

### Show Successful Operation
# Shows connection and email sending
docker compose logs mindfuel-quotes

### Show Database Health
# Shows database is ready
docker compose ps mindfuel-db

### Show Data Persistence
# Shows users in database
docker compose exec mindfuel-db psql -U postgres -d mindfuel_db -c "SELECT * FROM users;"

## Complete Workflow Example
# 1. Start services
docker compose up -d --build

# 2. Wait for services to be ready (check status)
docker compose ps

# 3. Initialize database
docker compose exec mindfuel-quotes python db_setup.py

# 4. Verify users added
docker compose exec mindfuel-db psql -U postgres -d mindfuel_db -c "SELECT * FROM users;"

# 5. Send quotes
docker compose exec mindfuel-quotes python main.py

# 6. Check logs
docker compose logs -f

# 7. Stop services
docker compose down

## Quick Reference

|Action        |Command                                                          |

|--------------|-----------------------------------------------------------------|

|Start services|`docker compose up -d --build`                                   |

|Stop services |`docker compose down`                                            |

|View status   |`docker compose ps`                                              |

|View logs     |`docker compose logs -f`                                         |

|Initialize DB |`docker compose exec mindfuel-quotes python db_setup.py`         |

|Send emails   |`docker compose exec mindfuel-quotes python main.py`             |

|Query database|`docker compose exec mindfuel-db psql -U postgres -d mindfuel_db`|

|Restart       |`docker compose restart`                                         |

|Fresh start   |`docker compose down -v && docker compose up -d --build`         |

## Common Error Solutions

### “Container name already in use”
docker compose down

docker rm -f mindfuel-db mindfuel-quotes

docker compose up -d --build

### “Service is not running”
docker compose ps

docker compose up -d

### “Table does not exist”
docker compose exec mindfuel-quotes python db_setup.py

### “Can’t connect to database”
docker compose restart mindfuel-db

docker compose logs mindfuel-db

-----

Pro Tip: Use docker compose logs -f to watch logs in real-time while testing!
