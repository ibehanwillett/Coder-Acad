from setup import db, ma
from datetime import datetime
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='comments')

    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
    card = db.relationship('Card', back_populates='comments')


class CommentSchema(ma.Schema):
    # Tell Marshmallow to nest a UserSchema instance when serializing
    user = fields.Nested('UserSchema', only=['id', 'name'])
    card = fields.Nested('CardSchema', only=['id', 'title'])

    class Meta:
        fields = ("id", "message", "user", "card")