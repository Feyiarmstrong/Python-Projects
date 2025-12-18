# Task 1: Containerize Python Email Delivery Service

## Overview

Containerizing the MindFuel quote delivery service into a portable Docker image. The service fetches motivational quotes from ZenQuotes API and emails them to subscribers daily.

## What the Application Does

- Fetches random quotes from ZenQuotes API
- Connects to PostgreSQL database
- Retrieves active subscribers
- Sends personalized emails with quotes
- Logs all activities

## Files

Zenquotes/

├── Dockerfile

├── .env

├── .env.docker

├── requirements.txt

├── main.py

├── db_setup.py

├── fetch_quote.py

├── send_email.py

├── logger_module.py

└── logs/

## Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code

COPY . .

# Run the app

CMD ["python", "main.py"]

## Environment Variables

Create .env.docker file:

DB_HOST

DB_NAME

DB_USER

DB_PASSWORD

DB_PORT=5432

ddb_email=your-email@gmail.com

ddb_password=your-app-password

## Building the Image
# Build the Docker image
docker build -t mindfuel-quotes:latest .

# Verify image was created
docker images | grep mindfuel-quotes

## Running the Container

### With Docker Run
# Run with environment file
docker run --env-file .env.docker --network your-network-name mindfuel-quotes:latest

# Run with manual environment variables
docker run \
  -e DB_HOST=your-db-host \
  -e DB_NAME=your-db-name \
  -e DB_USER=your-user \
  -e DB_PASSWORD=your-password \
  -e ddb_email=your-email@gmail.com \
  -e ddb_password=your-app-password \
  --network your-network-name \
  mindfuel-quotes:latest

### Network Setup
# Create a network for the app and database
docker network create mindfuel-network

# Run PostgreSQL database
docker run -d \
  --name mindfuel-db \
  --network mindfuel-network \
  -e POSTGRES_DB=mindfuel_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=your postgres password \
  -p 5432:5432 \
  postgres:15-alpine

# Run the application
docker run --env-file .env.docker --network mindfuel-network mindfuel-quotes:latest

## Testing the Container

### Verify Container Works
# Check logs
docker logs <container-id>

# Expected output:
Database connected successfully!

Fetched quote: "..." — Author

Email sent to user@example.com

### Verify Database Connection
# Connect to the database
docker exec -it mindfuel-db psql -U postgres -d mindfuel_db

# Check users
SELECT * FROM users;

## Publishing to Docker Hub

### 1. Tag the Image
docker tag mindfuel-quotes:latest your-username/mindfuel-quotes:latest

### 2. Login to Docker Hub
docker login

### 3. Push the Image
docker push your-username/mindfuel-quotes:latest

### 4. Verify on Docker Hub

Visit https://hub.docker.com/r/your-username/mindfuel-quotes

## Task Requirements Met

✅ Dockerfile created:

- Uses lightweight base image (python:3.11-slim)
- Installs all dependencies
- Sets environment variables
- Copies application code
- Clear entrypoint (CMD [“python”, “main.py”])

✅ Image built locally:

- Successfully builds without errors
- Image is portable and reproducible

✅ Container tested:

- Fetches quotes from API ✅
- Connects to database ✅
- Sends emails successfully ✅

✅ Image published:

- Pushed to Docker Hub or container registry

## Common Commands
# Build
docker build -t mindfuel-quotes:latest .

# Run
docker run --env-file .env.docker --network mindfuel-network mindfuel-quotes:latest

# Check running containers
docker ps

# View logs
docker logs <container-id>

# Stop container
docker stop <container-id>

# Remove container
docker rm <container-id>

# Remove image
docker rmi mindfuel-quotes:latest

## Troubleshooting

Can’t connect to database:

- Ensure database container is running
- Check network connectivity
- Verify environment variables are correct

Email not sending:

- Check email credentials in .env.docker
- Verify Gmail app password is correct
- Ensure 2FA is enabled on Gmail

Build fails:

- Check Dockerfile syntax
- Ensure all files exist
- Verify requirements.txt is complete
