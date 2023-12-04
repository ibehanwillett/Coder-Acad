from setup import db, ma
from datetime import datetime
from marshmallow import fields
from marshmallow.validate import OneOf, Regexp, Length, And

VALID_STATUSES = ('To Do', 'Done', 'Testing', 'Deployed', 'Cancelled')
class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(30), default='To Do')
    date_created = db.Column(db.Date, default=datetime.now().strftime('%Y-%m-%d'))

    # Foreign key - establishes a relationship at the database level
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # SQLAlchemy relationship - nests an instance of a User model in this one
    user = db.relationship('User', back_populates='cards')
    comments = db.relationship('Comment', back_populates='card')


class CardSchema(ma.Schema):
    # Tell Marshmallow to nest a UserSchema instance when serializing
    user = fields.Nested('UserSchema', exclude=['password'])
    comments = fields.Nested('CommentSchema', many=True, exclude=['card'])
    status = fields.String(validate=OneOf(VALID_STATUSES))
    title = fields.String(required=True, validate=And(
        Regexp('^[0-9a-zA-Z +$]', error='Title must contain only letters, numbers and spaces'),
        Length(min=3, error='Title must be at least 3 characters long')))

    class Meta:
        fields = ("id", "title", "description", "status", "date_created", "user", "comments")