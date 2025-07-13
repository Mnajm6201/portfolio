#!/bin/bash


# Navigate to project directory
cd ~/portfolio || {
  echo "Project folder not found!"
  exit 1
}

# Reset local repo to match main branch
git fetch && git reset origin/main --hard

# Activate virtual environment, install dependencies
source venv/bin/activate
pip install -r requirements.txt

# Restart the systemd service
systemctl daemon-reload
systemctl restart myportfolio