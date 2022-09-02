from class_models_and_db.models import User, Offer, Order
from functions.utils import load_users, load_offers, load_orders
from global_variables import db


def created_dbase():

    db.drop_all()
    db.create_all()

    users = [User(**user_data) for user_data in load_users()]
    order = [Order(**order_data) for order_data in load_orders()]
    offer = [Offer(**offer_data) for offer_data in load_offers()]

    db.session.add_all(users)
    db.session.add_all(order)
    db.session.add_all(offer)

    db.session.commit()
