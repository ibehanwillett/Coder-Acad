from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from models.user import User, UserSchema
from setup import bcrypt, db
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
from auth import admin_required


users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/register', methods=['POST'])
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
   
@users_bp.route('/login', methods=['POST'])
def login():
    # 1. Parse incoming POST body through schema
    user_info = UserSchema(exclude=['id', 'name','is_admin']).load(request.json)
    # 2. Select user with email that matches one in POST body
    stmt = db.select(User).where(User.email == user_info['email'])
    user = db.session.scalar(stmt)
    # 3. Check the password hash
    if user and bcrypt.check_password_hash(user.password, user_info['password']):
        # 4. Create a JWT 
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        # 5. Return the token
        return {'token': token, 'user': UserSchema(exclude=['password', 'cards']).dump(user)}
    else:
        return {'error':'Invalid password or email'}, 401

@users_bp.route('/')
@jwt_required()
def all_users():
    admin_required()
    # select * from cards;
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=['password']).dump(users)