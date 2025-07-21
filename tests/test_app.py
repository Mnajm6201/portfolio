# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # TODO Add more tests relating to the home page
        assert "Home" in html
        assert "Experience" in html
        assert "Education" in html
        assert "Projects" in html
        assert "Hobbies" in html
        assert "Timeline" in html
        assert "Contact" in html
        assert 'img/logo.svg' in html


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis

        # Test POST valid data
        post_response = self.client.post("/api/timeline_post", data={
            "name": "Test User",
            "email": "test@example.com",
            "content": "Testing, Testing, 1,2 ... 3?"
        })
        assert post_response.status_code == 200
        post_json = post_response.get_json()
        assert post_json["name"] == "Test User"
        assert post_json["email"] == "test@example.com"
        assert post_json["content"] == "Testing, Testing, 1,2 ... 3?"

        # Test GET again
        response = self.client.get("/api/timeline_post")
        json = response.get_json()
        assert len(json["timeline_posts"]) == 1
        timeline_post = json["timeline_posts"][0]
        assert timeline_post["name"] == "Test User"
        assert timeline_post["email"] == "test@example.com"
        assert timeline_post["content"] == "Testing, Testing, 1,2 ... 3?"
        assert "created_at" in timeline_post

        # Test ordering
        self.client.post("/api/timeline_post", data={
            "name": "Second User",
            "email": "second@example.com",
            "content": "Second post"
        })
        response = self.client.get("/api/timeline_post")
        json = response.get_json()
        assert len(json["timeline_posts"]) == 2
        assert json["timeline_posts"][0]["name"] == "Second User"
        assert json["timeline_posts"][1]["name"] == "Test User"

        # Test invalid POST
        bad_response = self.client.post("/api/timeline_post", data={
            "name": "Bad User",
            "email": "bad@example.com"
            # Missing 'content'
        })
        assert bad_response.status_code == 400 or bad_response.status_code == 422

        # TODO Add more tests relating to the timeline page

        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline - MLH Fellow</title>" in html
        for item in ["Home", "Experience", "Education", "Projects", "Hobbies", "Timeline", "Contact"]:
            assert item in html
        assert '<form' in html
        assert 'name="name"' in html
        assert 'name="email"' in html
        assert 'name="content"' in html or '<textarea' in html
        assert 'img/logo.svg' in html
    
    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html