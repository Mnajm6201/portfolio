#!/bin/bash


# Navigate to project directory
cd ~/portfolio || {
  echo "Project folder not found!"
  exit 1
}

# Reset local repo to match main branch
git fetch && git reset origin/main --hard

# spin containers down to prevent out of memory issues
docker compose -f docker-compose.prod.yml down

# Rebuild and start container
docker compose -f docker-compose.prod.yml up -d --build