from setup import db, ma
from datetime import datetime

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    status = db.Column(db.String(30), default='To Do')
    date_created = db.Column(db.Date, default=datetime.now().strftime("%Y-%m-%d"))

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date_created')