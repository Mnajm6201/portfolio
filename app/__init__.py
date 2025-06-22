import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Menu configuration
MENU_ITEMS = [
    {'name': 'Home', 'url': '/', 'endpoint': 'index'},
    {'name': 'Experience', 'url': '/experience', 'endpoint': 'experience'},
    {'name': 'Education', 'url': '/education', 'endpoint': 'education'},
    {'name': 'Projects', 'url': '/projects', 'endpoint': 'projects'},
    {'name': 'Hobbies', 'url': '/hobbies', 'endpoint': 'hobbies'},
    {'name': 'Contact', 'url': '/contact', 'endpoint': 'contact'},
]

# Make menu available to all templates
@app.context_processor
def inject_menu():
    return dict(menu_items=MENU_ITEMS)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

# Empty pages for now
@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience - MLH Fellow", url=os.getenv("URL"))

@app.route('/education')
def education():
    return render_template('education.html', title="Education - MLH Fellow", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects - MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies - MLH Fellow", url=os.getenv("URL"))

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact - MLH Fellow", url=os.getenv("URL"))