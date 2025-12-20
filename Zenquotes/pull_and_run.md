# MindFuel Quote Delivery - Pull and Run Instructions

## Image Information

Docker Hub Repository: feyiarmstrong/mindfuel-quotes

Image URL: https://hub.docker.com/r/feyiarmstrong/mindfuel-quotes

Full Image Tag: feyiarmstrong/mindfuel-quotes:latest

## Prerequisites

- Docker installed and running
- .env or .env.docker file with required environment variables
- Network access to database (if running separately)

## Environment Variables Required

Create a .env file with the following variables:

DB_HOST=your-database-host

DB_NAME=mindfuel_db

DB_USER

DB_PASSWORD

DB_PORT=5432

ddb_email= email@gmail.com
ddb_password= the app password

## Pulling the Image

### Pull Latest Version
docker pull feyiarmstrong/mindfuel-quotes:latest

### Verify Image Downloaded
docker images | grep mindfuel-quotes

Expected output:
feyiarmstrong/mindfuel-quotes   latest   abc123def456   2 hours ago   180MB

## Running the Container

### Basic Run (With Environment File)
docker run --name mindfuel-quotes --env-file .env feyiarmstrong/mindfuel-quotes:latest

### Run and Auto-Remove After Completion
docker run --rm --name mindfuel-quotes --env-file .env feyiarmstrong/mindfuel-quotes:latest

Flags Explained:

- --rm - Automatically removes container after it exits
- --name mindfuel-quotes - Names the container for easy reference
- --env-file .env - Loads environment variables from file

### Run with Network (If Database is in Docker)
docker run --rm --name mindfuel-quotes --env-file .env --network mindfuel-network feyiarmstrong/mindfuel-quotes:latest

### Run with Manual Environment Variables
docker run --rm \
  --name mindfuel-quotes \
  -e DB_HOST=your-db-host \
  -e DB_NAME=mindfuel_db \
  -e DB_USER=postgres \
  -e DB_PASSWORD=the password used \
  -e DB_PORT=5432 \
  -e ddb_email=your-email@gmail.com \
  -e ddb_password=your-app-password \
  feyiarmstrong/mindfuel-quotes:latest

## Complete Setup Example

### 1. Set Up Database Container (If Needed)
# Create network
docker network create mindfuel-network

# Run PostgreSQL database
docker run -d \
  --name mindfuel-db \
  --network mindfuel-network \
  -e POSTGRES_DB=mindfuel_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres password\
  -p 5432:5432 \
  postgres:15-alpine

### 2. Initialize Database
# Connect to database and create users table
docker exec -it mindfuel-db psql -U postgres -d mindfuel_db

# Run in psql:
CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100) NOT NULL,
    
    email VARCHAR(150) UNIQUE NOT NULL,
    
    is_active BOOLEAN DEFAULT TRUE,
    
    frequency VARCHAR(20) DEFAULT 'daily',
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

# Add sample users
INSERT INTO users (name, email, is_active) VALUES

('John Doe', 'john@example.com', TRUE),

('Jane Smith', 'jane@example.com', TRUE);

# Exit
\q

### 3. Pull and Run Application
# Pull the image
docker pull feyiarmstrong/mindfuel-quotes:latest

# Update .env with correct DB_HOST
echo "DB_HOST=mindfuel-db" > .env

echo "DB_NAME=mindfuel_db" >> .env

echo "DB_USER=postgres" >> .env

echo "DB_PASSWORD=postgres" >> .env

echo "DB_PORT=5432" >> .env

echo "ddb_email=email@gmail.com" >> .env

echo "ddb_password=app-password" >> .env

# Run the application
docker run --rm \
  --name mindfuel-quotes \
  --env-file .env \
  --network mindfuel-network \
  feyiarmstrong/mindfuel-quotes:latest

## Verifying Execution

### Check Logs
# If container is still running
docker logs mindfuel-quotes

# If you didn't use --rm flag
docker logs mindfuel-quotes

### Expected Output
Database connected successfully!

Fetched quote: "Success is not final, failure is not fatal..." — Winston Churchill

Email sent to john@example.com

Email sent to jane@example.com

### Check Container Status
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

## Common Use Cases

### Run Once and Clean Up
docker run --rm --name mindfuel-quotes --env-file .env --network mindfuel-network feyiarmstrong/mindfuel-quotes:latest

### Keep Container for Debugging
# Run without --rm

Feyiarmstrong, [12/20/2025 5:56 PM]

docker run --name mindfuel-quotes --env-file .env --network mindfuel-network feyiarmstrong/mindfuel-quotes:latest

# Check logs after execution
docker logs mindfuel-quotes

# Clean up when done
docker rm mindfuel-quotes

### Run with Detached Mode (Background)
docker run -d --name mindfuel-quotes --env-file .env --network mindfuel-network feyiarmstrong/mindfuel-quotes:latest

# View logs
docker logs -f mindfuel-quotes

## Troubleshooting

### Image Pull Fails
# Verify Docker Hub connection
docker login

# Try pulling again
docker pull feyiarmstrong/mindfuel-quotes:latest

### Container Exits Immediately
# Check logs for errors
docker logs mindfuel-quotes

# Common issues:
- Database not accessible (check DB_HOST)
- Missing environment variables
- Network not configured

### Can’t Connect to Database
# Verify database is running
docker ps | grep mindfuel-db

# Check network
docker network inspect mindfuel-network

# Test database connection
docker exec -it mindfuel-db psql -U postgres -d mindfuel_db -c "SELECT 1;"

### Email Not Sending

- Verify email credentials in .env file
- Check if Gmail App Password is correct
- Ensure 2-Factor Authentication is enabled
- Check logs: docker logs mindfuel-quotes

## Cleaning Up

### Remove Container
docker rm mindfuel-quotes

### Remove Image
docker rmi feyiarmstrong/mindfuel-quotes:latest

### Remove All (Container, Network, Database)
docker rm -f mindfuel-quotes mindfuel-db

docker network rm mindfuel-network

## Quick Reference

|Action          |Command                                                                                          |

|----------------|-------------------------------------------------------------------------------------------------|

|Pull image      |`docker pull feyiarmstrong/mindfuel-quotes:latest`                                               |

|Run once        |`docker run --rm --env-file .env feyiarmstrong/mindfuel-quotes:latest`                           |

|Run with network|`docker run --rm --env-file .env --network mindfuel-network feyiarmstrong/mindfuel-quotes:latest`|

|View logs       |`docker logs mindfuel-quotes`                                                                    |

|Remove container|`docker rm mindfuel-quotes`                                                                      |

## Additional Information

Image Size: ~180MB (Python 3.11 slim base)

Base Image: python:3.11-slim

Entry Point: python main.py

Dependencies: Listed in requirements.txt (psycopg2, requests, python-dotenv, etc.)

-----

Docker Hub: https://hub.docker.com/r/feyiarmstrong/mindfuel-quotes

For issues or questions, check the logs: docker logs mindfuel-quotes
