from setup import db, bcrypt
from models.user import User
from models.card import Card
from datetime import date
from flask import Blueprint
from models.comments import Comment

db_commands = Blueprint('db', __name__)
@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")


@db_commands.cli.command("seed")
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

    db.session.add_all(users)
    db.session.commit()

    cards = [
        Card(
            title="Start the project",
            description="Stage 1 - ERD Creation",
            status='Done',
            date_created=date.today(),
            user_id = users[0].id
        ),
        Card(
            title="ORM Queries",
            description="Stage 2 - Implement CRUD queries",
            status='In Progress',
            date_created=date.today(),
            user_id = users[1].id
        ),
        Card(
            title="Marshmallow",
            description="Stage 3 - Implement JSONify of models",
            status='In Progress',
            date_created=date.today(),
            user_id = users[0].id,
        ),
    ]

    db.session.add_all(cards)
    db.session.commit()

    comments = [
        Comment(
            message = 'comment 1',
            user_id=users[0].id,
            card_id=cards[1].id
        ),

        Comment(
            message = 'comment 2',
            user_id=users[1].id,
            card_id=cards[1].id
        ),

        Comment(
            message = 'comment 3',
            user_id=users[1].id,
            card_id=cards[0].id
        ),
    ]
    db.session.add_all(comments)
    db.session.commit()
    print("Database seeded")
