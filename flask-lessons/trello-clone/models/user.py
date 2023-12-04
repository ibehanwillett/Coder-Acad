from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, default='Anonymous')
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    cards = db.relationship('Card', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')


class UserSchema(ma.Schema):
    cards = fields.Nested('CardSchema', exclude=['user'], many=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=Length(min=8, error="Password must be at least 8 characters"))


    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "cards")