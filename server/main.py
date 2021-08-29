from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import os

# Init web app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
connection_path = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# Init database
app.config['SQLALCHEMY_DATABASE_URI'] = connection_path
engine = create_engine(connection_path)
sess = scoped_session(sessionmaker(bind=engine))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Many-to-Many relationship between reviewers and applications
reviewers = db.Table('reviewers',
    db.Column('application_id', db.Integer, db.ForeignKey('reviewer.id'), primary_key=True),
    db.Column('reviewer_id', db.Integer, db.ForeignKey('application.id'), primary_key=True)
)

# Reviewer class
list_len = 1000
class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(60), nullable=False)
    area_expertise = db.Column(db.String(list_len), nullable=False) # Holds array
    research_expertise = db.Column(db.String(list_len), nullable=False) # Holds array
    area_research = db.Column(db.String(list_len), nullable=False) # Holds array
    
    def __init__(self, first_name,last_name, gender, area_expertise, research_expertise, area_research):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.area_expertise = area_expertise
        self.research_expertise = research_expertise
        self.area_research = area_research

    def __repr__(self):
        return f'<Reviewer {self.name} id={self.id}>'

    def create(self):
        '''creates reviewer, and returns it as well'''
        db.session.add(self)
        db.session.commit()
        return self

class ReviewerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Reviewer
        include_relationships=True
        load_instance=True

# Application class

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    investigator = db.Column(db.String(100), unique=True, nullable=False)
    institution = db.Column(db.String(60), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    primary_type_research = db.Column(db.String(60), nullable=False)
    secondary_type_research = db.Column(db.String(60))
    area_research = db.Column(db.String(list_len), nullable=False) # Holds array
    keywords = db.Column(db.String(list_len), nullable=False) # Holds array
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

    def create(self):
        '''creates application, and returns it as well'''
        db.session.add(self)
        db.session.commit()
        return self

class ApplicationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Application
        include_relationships=True
        load_instance=True

def crud_post(content,ModelSchema):
    schema = ModelSchema()
    data = schema.load(content,session=sess)
    return jsonify(schema.dump(data.create()))

def crud_get(id,ModelClass,ModelSchema):
    get_data = ModelClass.query.get(id)
    schema = ModelSchema()
    application = schema.dump(get_data)
    return jsonify(application)

def crud_update(id,changes,ModelClass,ModelSchema):
    clean_changes = {key:val for key,val in changes.items() if key != 'id'}
    get_data = ModelClass.query.get(id)
    schema = ModelSchema()
    valid_keys = {key for key in get_data.__dict__.keys() if not key.startswith("_")}
    for key,val in clean_changes.items():
        if key in valid_keys:
            get_data.__setattr__(key,val)

    db.session.add(get_data)
    db.session.commit()
    return jsonify(schema.dump(get_data))

def crud_delete(id,ModelClass):
    data = ModelClass.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({"id" : id})

def crud_get_all(ModelClass,ModelSchema):
    schema = ModelSchema()
    all_data = ModelClass.query.all()
    json_clean = [schema.dump(data) for data in all_data]
    return jsonify(json_clean)

class CRUD:
    def __init__(self,ModelClass,ModelSchema,route):
        self.ModelClass = ModelClass
        self.ModelSchema = ModelSchema
        self.route = route
        self.add_routes()
    def add_routes(self):
        id_route = f'{self.route}/<id>'

        @app.route(id_route,methods=["GET"],endpoint=f'{self.route}-get')
        def get(id):
            return crud_get(id,self.ModelClass,self.ModelSchema)

        @app.route(self.route,methods=["POST"],endpoint=f'{self.route}-post')
        def post():
            return crud_post(request.json,self.ModelSchema)

        @app.route(id_route,methods=['PUT'],endpoint=f'{self.route}-put')
        def put(id):
            return crud_update(id, request.json, self.ModelClass, self.ModelSchema)

        @app.route(id_route,methods=['DELETE'],endpoint=f'{self.route}-delete')
        def delete(id):
            return crud_delete(id, self.ModelClass)

        @app.route(self.route,methods=['GET'],endpoint=f'{self.route}-gets')
        def get_all():
            return crud_get_all(self.ModelClass,self.ModelSchema)



# Routes
@app.route("/", methods=["GET"])
def home():
    return "API is up and running!"

    
if __name__ == "__main__":

    # Setup database
    
    db.create_all()
    application_crud = CRUD(Application, ApplicationSchema, '/application')
    reviewer_crud = CRUD(Reviewer,ReviewerSchema,'/reviewer')

    # Start the web server
    app.run(debug=True)
