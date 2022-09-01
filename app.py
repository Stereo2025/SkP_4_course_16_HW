from flask import current_app, jsonify
from class_models_and_db.create_db import create_dbase
from users_bprint.views import user_blueprint
from orders_bprint.views import order_blueprint
from offers_bprint.views import offer_blueprint

app = current_app

create_dbase()

app.register_blueprint(user_blueprint)
app.register_blueprint(order_blueprint)
app.register_blueprint(offer_blueprint)


@app.errorhandler(404)
def page_400_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return jsonify({"Error": 'Information Not Found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
