from setup import db, ma
from datetime import datetime
from marshmallow import fields

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    status = db.Column(db.String(30), default='To Do')
    date_created = db.Column(db.Date, default=datetime.now().strftime("%Y-%m-%d"))

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False) #not model name, table name
    user = db.relationship('User', back_populates='cards') # first parameter is model name

    # comment_id = db.Column(db.Integer(), db.ForeignKey('comments.id'))
    comments = db.relationship('Comment', back_populates='card')
# cards- the name of the variable holding the db.relatiomship

class CardSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password'])
    comments = fields.Nested('CommentSchema', many=True, exclude=['card'])

    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date_created', 'user')