#!/bin/bash
set -e

./install.sh

echo "App and container setup complete. Container should be running on port 8000."
echo "Use 'docker logs fastapi-notifications-app' to check logs."
