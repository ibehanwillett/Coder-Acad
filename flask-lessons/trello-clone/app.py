from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import date, timedelta
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from os import environ

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://trello_dev:spameggs123@127.0.0.1:5432/trello' # Connector string

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt= Bcrypt(app)
jwt = JWTManager(app)

def admin_required():
    user_email = get_jwt_identity()
    stmt = db.select(User).where(User.email == user_email)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        return abort(401)
    
@app.errorhandler(401)
def unauthorized(err):
    return {'error': 'You are not authorized to access this resource'},401

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    status = db.Column(db.String(30))
    date_created = db.Column(db.Date())

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date_created')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
# default will be handled by Alchemy.

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

@app.cli.command("db_create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")


@app.cli.command("db_seed")
def db_seed():
    users= [
        User(
            email='admin@spam.com',
            password=bcrypt.generate_password_hash('swordfish').decode('utf8'),
            is_admin=True
        ),
        User(
            name='John Cleese',
            email='cleese@spam.com',
            password=bcrypt.generate_password_hash('tisbutascratch').decode('utf8'),
        )
    ]

    cards = [
        Card(
            title="Start the project",
            description="Stage 1 - ERD Creation",
            status='Done',
            date_created=date.today(),
        ),
        Card(
            title="ORM Queries",
            description="Stage 2 - Implement CRUD queries",
            status='In Progress',
            date_created=date.today(),
        ),
        Card(
            title="Marshmallow",
            description="Stage 3 - Implement JSONify of models",
            status='In Progress',
            date_created=date.today(),
        ),
    ]

    db.session.add_all(users)
    db.session.add_all(cards)
    db.session.commit()

    print("Database seeded")

@app.route('/users/register', methods=['POST'])
def register():
    try:
        # Parse incoming POST body through schema
        user_info = UserSchema(exclude=['id','is_admin']).load(request.json)
        # Create a new user with parsed data
        user = User(
            email=user_info['email'],
            password=bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
            name=user_info.get('name','')
        )

        # Add & commit the new user to the database
        db.session.add(user)
        db.session.commit()

        # Return the new user
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'},409
   
@app.route('/users/login', methods=['POST'])
def login():
    # 1. Parse incoming POST body through schema
    user_info = UserSchema(exclude=['id', 'name','is_admin']).load(request.json)
    # 2. Select user with email that matches one in POST body
    stmt = db.select(User).where(User.email == user_info['email'])
    user = db.session.scalar(stmt)
    # 3. Check the password hash
    if user and bcrypt.check_password_hash(user.password, user_info['password']):
        # 4. Create a JWT 
        token = create_access_token(identity=user.email, expires_delta=timedelta(hours=2))
        # 5. Return the token
        return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
    else:
        return {'error':'Invalid password or email'}, 401

@app.route('/cards')
@jwt_required()
def all_cards():
    admin_required()
    # select * from cards;
    stmt = db.select(Card)
        # .where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards)



@app.route("/")
def index():
    return "Hello world!"

# @app.errorhandler(IntegrityError)
# def integrity_error(err):
#     return {'error': err.__dict__},409

