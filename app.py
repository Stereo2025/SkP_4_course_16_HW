from flask import jsonify, Flask
from global_variables import db
from class_models_and_db.create_db import created_dbase
from users_bprint.views import user_blueprint
from orders_bprint.views import order_blueprint
from offers_bprint.views import offer_blueprint


app = Flask(__name__)

app.json.ensure_ascii = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hw_16_bprint_db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(user_blueprint)
app.register_blueprint(order_blueprint)
app.register_blueprint(offer_blueprint)

db.init_app(app)
app.app_context().push()
created_dbase()


@app.errorhandler(404)
def page_400_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return jsonify({"Error": 'Information Not Found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
