from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Init web app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Init database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Many-to-Many relationship between reviewers and applications
reviewers = db.Table('reviewers',
    db.Column('application_id', db.Integer, db.ForeignKey('reviewer.id'), primary_key=True),
    db.Column('reviewer_id', db.Integer, db.ForeignKey('application.id'), primary_key=True)
)

# Reviewer class

class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    gender = db.Column(db.String(60), nullable=False)
    area_expertise = db.Column(db.PickleType(), nullable=False) # Holds array
    research_expertise = db.Column(db.PickleType(), nullable=False) # Holds array
    area_research = db.Column(db.PickleType(), nullable=False) # Holds array
    
    def __init__(self, name, gender, area_expertise, research_expertise, area_research):
        self.name = name
        self.gender = gender
        self.area_expertise = area_expertise
        self.research_expertise = research_expertise
        self.area_research = area_research

# Application class

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    investigator = db.Column(db.String(100), unique=True, nullable=False)
    institution = db.Column(db.String(60), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    primary_type_research = db.Column(db.String(60), nullable=False)
    secondary_type_research = db.Column(db.String(60))
    area_research = db.Column(db.PickleType(), nullable=False) # Holds array
    keywords = db.Column(db.PickleType(), nullable=False) # Holds array
    reviewers = db.relationship('Reviewer', secondary=reviewers, lazy='subquery',
        backref=db.backref('applications', lazy=True))

    def __init__(self, investigator, institution, title, primary_type_research, secondary_type_research, area_research, keywords, reviewers):
        self.investigator = investigator
        self.institution = institution
        self.title = title
        self.primary_type_research = primary_type_research
        self.secondary_type_research = secondary_type_research
        self.area_research = area_research
        self.keywords = keywords
        self.reviewers = reviewers


# Routes
@app.route("/", methods=["GET"])
def home():
    return "API is up and running!"

@app.route("/application/new", methods=["POST"])
def new_application():
    return {}
    
if __name__ == "__main__":

    # Setup database
    db.create_all()

    # Start the web server
    app.run(debug=True)