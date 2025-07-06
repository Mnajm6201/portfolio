#!/bin/bash

# Kill all existing tmux sessions
tmux kill-server 2>/dev/null

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

# Start new tmux session running the Flask app
tmux new-session -d -s flask-session "source venv/bin/activate && flask run --host=0.0.0.0"