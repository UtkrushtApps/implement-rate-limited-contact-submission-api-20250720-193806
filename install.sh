#!/bin/bash
set -e

# Build the Docker image
echo "Building Docker image..."
docker build -t fastapi-notifications .

echo "Image built. Starting container..."
# Start (remove any existing container with same name)
if [ $(docker ps -a -q -f name=fastapi-notifications-app) ]; then
    docker rm -f fastapi-notifications-app
fi

docker run -d --name fastapi-notifications-app -p 8000:8000 fastapi-notifications

echo "Container started."
