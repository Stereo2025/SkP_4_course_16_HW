from global_variables import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50), unique=True)
    role = db.Column(db.String(10))
    phone = db.Column(db.String(15), unique=True)


class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(100))
    start_date = db.Column(db.String(15))
    end_date = db.Column(db.String(15))
    address = db.Column(db.String(150))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey(User.id))
    executor_id = db.Column(db.Integer, db.ForeignKey(User.id))


class Offer(db.Model):

    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id))
    executor_id = db.Column(db.Integer, db.ForeignKey(User.id))
