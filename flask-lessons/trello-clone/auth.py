from flask_jwt_extended import get_jwt_identity
from models.user import User
from flask import abort
from setup import db

def admin_required():
    user_email = get_jwt_identity()
    stmt = db.select(User).where(User.email == user_email)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        return abort(401)