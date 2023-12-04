from flask import Blueprint
from setup import db, bcrypt
from models.card import Card
from models.user import User
from models.comment import Comment
from datetime import date


db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def db_create():
    db.drop_all()
    db.create_all()
    print("Created tables")


@db_commands.cli.command("seed")
def db_seed():
    # Users
    users = [
        User(
            email="admin@spam.com",
            password=bcrypt.generate_password_hash("spinynorman").decode("utf8"),
            is_admin=True,
        ),
        User(
            name="John Cleese",
            email="cleese@spam.com",
            password=bcrypt.generate_password_hash("tisbutascratch").decode("utf8"),
        ),
    ]

    db.session.add_all(users)
    db.session.commit()

    # Cards
    cards = [
        Card(
            title="Start the project",
            description="Stage 1 - ERD Creation",
            status="Done",
            date_created=date.today(),
            user_id = users[0].id
        ),
        Card(
            title="ORM Queries",
            description="Stage 2 - Implement CRUD queries",
            status="In Progress",
            date_created=date.today(),
            user_id = users[1].id
        ),
        Card(
            title="Marshmallow",
            description="Stage 3 - Implement JSONify of models",
            status="In Progress",
            date_created=date.today(),
            user_id = users[0].id
        ),
    ]

    db.session.add_all(cards)
    db.session.commit()

    comments = [
        Comment(
            message="Comment 1",
            user_id=users[0].id,
            card_id=cards[1].id
        ),
        Comment(
            message="Comment 2",
            user_id=users[1].id,
            card_id=cards[1].id
        ),
        Comment(
            message="Comment 3",
            user_id=users[1].id,
            card_id=cards[0].id
        )
    ]

    db.session.add_all(comments)
    db.session.commit()

    print("Database seeded")