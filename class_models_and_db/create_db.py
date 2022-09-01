from class_models_and_db.models import User, Offer, Order, db
from functions.utils import load_users, load_offers, load_orders


def create_dbase():
    db.drop_all()
    db.create_all()

    users = [User(**row) for row in load_users()]
    orders = [Order(**row) for row in load_orders()]
    offers = [Offer(**row) for row in load_offers()]

    db.session.add_all(users)
    db.session.add_all(orders)
    db.session.add_all(offers)
    db.session.commit()


create_dbase()
