from flask import Blueprint, request
from setup import db
from models.card import Card, CardSchema
from flask_jwt_extended import jwt_required
from auth import admin_required

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

@cards_bp.route('/')
@jwt_required()
def all_cards():
    admin_required()
    # select * from cards;
    stmt = db.select(
        Card
        )
        # .where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards)

@cards_bp.route('/<int:id>/')
def one_card(id):
    admin_required()
    stmt = db.select(Card).filter_by(id=id)
    card = (db.session.scalar(stmt))
    if card: # If card is a truthy value, return
        return CardSchema().dump(card)
    else:
        return {'error':'Card not found'}, 404

@cards_bp.route('/', methods=['POST'])
def create_card():
    card_info = CardSchema(exclude=['id','date_created']).load(request.json)
    print(card_info)
    return {}
