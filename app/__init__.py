import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Experience data
EXPERIENCES = [
    {
        'title': 'Emerging Talent Intern – Software Engineering',
        'company': 'Metropolitan Transportation Authority (MTA)',
        'dates': 'Jun 2025 – Present',
        'description': [
            'Leading the build of a modern, accessible website for the Transit Electrical Apprenticeship program with React/Next.js and Spring Boot APIs, targeting a 50% boost in applicant engagement and SEO reach.',
            'Architecting a scalable PostgreSQL schema to centralize apprentice and employee records, enabling real-time querying of skills, certifications, and on-the-job progress.',
            'Developing an interactive learning portal that delivers on-demand modules to transit employees and tracks completion analytics for training leads.',
            'Creating a companion mobile digital sign-in sheet connected to a secure server, capturing daily hours and automating supervisor approvals across depots.'
        ],
        'image_path': 'experience_MTA.gif'
    },
    {
        'title': 'Production Engineering Fellow',
        'company': 'MLH × Meta',
        'dates': 'Jun 2025 – Present',
        'description': [
            'Engaged in a Meta-sponsored fellowship focused on site reliability: Linux internals, container orchestration, databases, CI/CD, monitoring, and incident response.',
            'Collaborating with Meta engineers and 20+ fellows in Agile sprints; implementing test pipelines to reach 90% code coverage.'
        ],
        'image_path': 'experience_MLH.gif'
    },
    {
        'title': 'Software Engineering Intern',
        'company': 'Unadat',
        'dates': 'Starting Jul 2025',
        'description': [
            'Expected to contribute to Python/Go micro-services, high-volume data pipelines, and CI/CD automation powering near-real-time insights for global brands.'
        ],
        'image_path': 'experience_unadat.png'
    },
    {
        'title': 'Data Science Fellow',
        'company': 'CUNY Tech Prep',
        'dates': 'Starting Aug 2025',
        'description': [
            'Selected for a year-long industry program emphasizing Python, SQL, machine-learning pipelines, and professional development.'
        ],
        'image_path': 'experience_ctp.png'
    },
    {
        'title': 'Fellow',
        'company': 'BASTA Fellowship',
        'dates': 'June 2025 – Present',
        'description': [
            'Participating in a career accelerator offering mentorship, technical interview prep, and support in building a competitive application profile',
            'Engaging in one-on-one coaching and cohort-based sessions focused on professional development and career exploration in tech'
        ],
        'image_path': 'experience_basta.jpg'
    },
    {
        'title': 'Software Engineering Fellow',
        'company': 'Headstarter AI',
        'dates': 'July 2024 – September 2024',
        'description': [
            'Engineered & deployed 5 AI-powered applications in 7 weeks, leveraging machine learning (NLP, RAG models) and full-stack frameworks, such as Next.js, MongoDB, Vercel and StripeAPI',
            'Led a team of three to develop an interactive code support bot using Next.js and a custom RAG pipeline.'
        ],
        'image_path': 'experience_headstarter.jpg'
    }
]

# Education data
EDUCATION = [
    {
        'school': 'CUNY Brooklyn College',
        'degree': 'B.S. Computer Science, B.S. Mathematics, Minor in Data Science',
        'dates': 'Expected May 2026',
        'gpa': '4.0/4.0 — Dean\'s List',
        'courses': [
            'Algorithm Analysis',
            'Statistics', 
            'Databases',
            'Software Engineering',
            'Machine Learning',
            'Artificial Intelligence',
            'Computer Architecture',
            'Web Applications',
            'Operating Systems'
        ],
        'image': 'education_brooklyn.webp'
    },
    {
        'school': 'Kingsborough Community College',
        'degree': 'Transfer Credits',
        'dates': 'Completed',
        'gpa': None,
        'courses': [
            'Linear Algebra',
            'Data Structures', 
            'Assembly Language',
            'Object Oriented Programming'
        ],
        'image': 'education_kingsborough.jpg'
    }
]

# Hobbies data
HOBBIES = [
    {
        'title': 'Reading',
        'description': "I read a lot - everything from fantasy and sci-fi to philosophy. Always have a book going and love finding new authors that make me think differently. My favorite book is The Brothers Karamazov, and I'm currently reading The Wheel of Time series (I'm on book five!)",
        'image': 'hobbies_reading.jpg'
    },
    {
        'title': 'Cinema',
        'description': "Big movie fan. I watch everything from blockbusters to foreign films. My Top four: The Godfather, Excalibur, Cinema Paradisio, and The Lord of the Rings series (yes that counts as one)",
        'image': 'hobbies_cinema.webp'
    },
    {
        'title': 'History',
        'description': "History is wild - real events are often crazier than fiction. I love learning about how we got to where we are today. I love reading any type of history, but I particularly love Greek and Roman antiquity.",
        'image': 'hobbies_history.webp'
    },
    {
        'title': 'Gaming',
        'description': "I play strategy games mostly, but also enjoy exploring new worlds and solving puzzles. Great way to relax and keep my mind sharp. My favorite games include Disco Elysium, Kingdom Come Deliverance, and Crusader Kings 3. I also love board games like Scythe and Catan, card games like Magic the Gathering, and RPGs like Dungeons and Dragons",
        'image': 'hobbies_gaming.webp'
    },
    {
        'title': 'Learning',
        'description': "Always picking up new skills or diving into random topics that catch my interest. Can't help being curious about how things work. Whether its learning a new langauge (French atm), a new tech stack, or a new obssession (making the PERFECT cup of coffee), I love getting lost in a rabbit hole, and coming out with a new skill, hobby or area of knowledge",
        'image': 'hobbies_learning.jpg'
    },
    {
        'title': 'Chess',
        'description': "Been playing chess for years. Love the mental challenge and trying to think a few moves ahead. I do not claim to be very good, but I do think I am good at getting better. My favorite openings are the Italian game ofr white, and the Caro Khan for black",
        'image': 'hobbies_chess.png'
    },
    {
        'title': 'Traveling',
        'description': "Enjoy exploring new places and experiencing different cultures. Good food and interesting conversations with locals are the best parts. I have not gotten to travel a great deal, but the places I have been will stay in my memories for ever. My favorite city is Istanbul",
        'image': 'hobbies_traveling.jpg'
    }
]

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

@app.route('/experience')
def experience():
    return render_template('experience.html', 
                         title="Experience - MLH Fellow", 
                         url=os.getenv("URL"),
                         experiences=EXPERIENCES)

@app.route('/education')
def education():
    return render_template('education.html', 
                         title="Education - MLH Fellow", 
                         url=os.getenv("URL"),
                         schools=EDUCATION)

@app.route('/projects')
def projects():
    return render_template('projects.html', 
                         title="Projects - MLH Fellow", 
                         url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', 
                         title="Hobbies - MLH Fellow", 
                         url=os.getenv("URL"),
                         hobbies=HOBBIES)

@app.route('/contact')
def contact():
    return render_template('contact.html', 
                         title="Contact - MLH Fellow", 
                         url=os.getenv("URL"))
