from flask import Blueprint, jsonify, request, abort
from class_models_and_db.models import Offer, db
from functions.utils import offer_serialize

offer_blueprint = Blueprint('offer_blueprint', __name__)


@offer_blueprint.get('/')
def response_page():

    return '<div style="background-color:black;color:white;padding:700px;">' \
           '<centre><h1>Сейчас вы на главной страничке, для того что бы перейти на нужную вкладку, необходимо ' \
           'ввести в адресной строке соответствующий запрос!</h1><centre>' \
           '</div>'


@offer_blueprint.get('/offers/')
def all_offers_page():
    """Выводит все данные из offers.json в json формате"""

    offers = Offer.query.all()
    return jsonify([offer_serialize(row) for row in offers])


@offer_blueprint.get('/offers/<int:uid>/')
def get_offer_uid(uid):
    """Выводит одно 'предложение' в json формате"""

    offers = Offer.query.get(uid)
    if not offers:
        return abort(404)

    return jsonify(offer_serialize(offers))


@offer_blueprint.post('/offers/')
def create_new_offer():
    """
    Добавляет предложение в таблицу offers.
    Заполнение происходит через json с помощью метода POST
    """

    query = request.json
    offer = Offer(
        order_id=query.get('order_id'),
        executor_id=query.get('executor_id')
    )
    db.session.add(offer)
    db.session.commit()
    return jsonify(offer_serialize(offer))


@offer_blueprint.put('/offers/<int:uid>/')
def change_offer_info(uid):
    """
    Получает конкретное предложение по его id.
    Обновляет данные о предложении в таблице данными из json,
    с помощью метода PUT.
    """

    offer = Offer.query.get(uid)
    if not offer:
        return abort(404)

    query = request.json

    offer.order_id = query.get('order_id')
    offer.executor_id = query.get('executor_id')

    db.session.add(offer)
    db.session.commit()

    return jsonify(offer_serialize(offer))


@offer_blueprint.delete('/offers/<int:uid>/')
def delete_offer(uid):
    """
    Получает пользователя по его id.
    Удаляет информацию о нём.
    """

    offer = Offer.query.get(uid)
    if not offer:
        return abort(404)

    db.session.delete(offer)
    db.session.commit()
    return jsonify({'Attention !': f'Offer into {uid} removed'})
#######################################################################################################################
