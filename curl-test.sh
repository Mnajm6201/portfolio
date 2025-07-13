#!/bin/bash

RANDOM_NUMBER=$RANDOM

# Create post
CREATE_RESPONSE=$(curl -s -X POST http://127.0.0.1:5000/api/timeline_post \
  -d "name=Mohammad" \
  -d "email=mohammadhnajm@gmail.com" \
  -d "content=I'm testing curl, here’s a random number: $RANDOM_NUMBER")

echo "$CREATE_RESPONSE"

# Extract ID
POST_ID=$(echo $CREATE_RESPONSE | grep -o '"id":[ ]*[0-9]*' | grep -o '[0-9]*')

# Get posts
curl -s http://127.0.0.1:5000/api/timeline_post

# Delete post
curl -s -X DELETE http://127.0.0.1:5000/api/timeline_post/$POST_ID