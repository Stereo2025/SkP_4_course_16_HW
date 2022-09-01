from flask import Blueprint, jsonify, request, abort
from class_models_and_db.models import Order, db
from functions.utils import order_serialize

order_blueprint = Blueprint('order_blueprint', __name__)


@order_blueprint.get('/')
def response_page():

    return '<div style="background-color:black;color:white;padding:700px;">' \
           '<centre><h1>Сейчас вы на главной страничке, для того что бы перейти на нужную вкладку, необходимо ' \
           'ввести в адресной строке соответствующий запрос!</h1><centre>' \
           '</div>'


@order_blueprint.get('/orders/')
def all_orders_page():
    """Выводит все данные из orders.json в json формате"""

    orders = Order.query.all()
    return jsonify([order_serialize(row) for row in orders])


@order_blueprint.get('/orders/<int:uid>/')
def get_orders_uid(uid):
    """Выводит один 'заказ' в json формате"""

    orders = Order.query.get(uid)
    if not orders:
        return abort(404)

    return jsonify(order_serialize(orders))


@order_blueprint.post('/orders/')
def create_new_order():
    """
    Добавляет заказ в таблицу orders.
    Заполнение происходит через json с помощью метода POST
    """

    query = request.json
    order = Order(
        name=query.get('name'),
        description=query.get('description'),
        start_date=query.get('start_date'),
        end_date=query.get('end_date'),
        address=query.get('address'),
        price=query.get('price'),
        customer_id=query.get('customer_id'),
        executor_id=query.get('executor_id')
    )
    db.session.add(order)
    db.session.commit()
    return jsonify(order_serialize(order))


@order_blueprint.put('/orders/<int:uid>/')
def changes_order_info(uid):
    """
    Получает конкретный заказ по его id.
    Обновляет данные о заказе в таблице данными из json,
    с помощью метода PUT.
    """

    order = Order.query.get(uid)
    if not order:
        return abort(404)

    query = request.json

    order.name = query.get('name')
    order.description = query.get('description')
    order.start_date = query.get('start_date')
    order.end_date = query.get('end_date')
    order.address = query.get('address')
    order.price = query.get('price')
    order.customer_id = query.get('customer_id')
    order.executor_id = query.get('executor_id')

    db.session.add(order)
    db.session.commit()

    return jsonify(order_serialize(order))


@order_blueprint.delete('/orders/<int:uid>/')
def delete_order(uid):
    """
    Получает заказ по его id.
    Удаляет информацию о нём.
    """

    order = Order.query.get(uid)
    if not order:
        return abort(404)

    db.session.delete(order)
    db.session.commit()
    return jsonify({'Attention !': f'Order into {uid} removed'})
#######################################################################################################################
