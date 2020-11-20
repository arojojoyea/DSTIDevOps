from flask import Flask, request, json, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://UE0kDnSijj:9klWE7urdT@remotemysql.com:3306/UE0kDnSijj'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://testaccount:enCap$ul8@localhost:3307/test_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://IcALVn1SW1:s23ZPO6lbB@remotemysql.com:3306/IcALVn1SW1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    __tablename__ = "purchase"
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(32))
    customer_number = db.Column(db.String(32))
    item_purchased = db.Column(db.String(32), unique=True)
    password = db.Column(db.Integer)
    quantity_purchased = db.Column(db.Integer)

    def __init__(self, item_purchased, password, customer_name, customer_number, quantity_purchased):
        self.item_purchased = item_purchased
        self.password = password
        self.customer_name = customer_name
        self.customer_number = customer_number
        self.quantity_purchased = quantity_purchased 

db.create_all()

class UserSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'item_purchased', 'password', 'customer_name', 'customer_number', 'quantity_purchased')

user_schema = UserSchema()
users_schema = UserSchema(many=True)




class HomePage(Resource):
    @staticmethod
    def get(): 
        return Response(response=json.dumps({"Message": "Welcome to DSTI Customer Purchase API"}),
                    status=200,
                    mimetype='application/json')


class CustomerManager(Resource):
    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            users = User.query.all()
            return jsonify(users_schema.dump(users))
        user = User.query.get(id)
        return jsonify(user_schema.dump(user))

    @staticmethod
    def post():
        item_purchased = request.json['item_purchased']
        password = request.json['password']
        customer_name = request.json['customer_name']
        customer_number = request.json['customer_number']
        quantity_purchased = request.json['quantity_purchased']

        user = User(item_purchased, password, customer_name, customer_number, quantity_purchased)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'Messquantity_purchased': f'User {customer_name} {customer_number} inserted.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Messquantity_purchased': 'Must provide the user ID' })
        user = User.query.get(id)

        item_purchased = request.json['item_purchased']
        password = request.json['password']
        customer_name = request.json['customer_name']
        customer_number = request.json['customer_number']
        quantity_purchased = request.json['quantity_purchased']

        user.item_purchased = item_purchased 
        user.password = password 
        user.customer_name = customer_name 
        user.customer_number = customer_number
        user.quantity_purchased = quantity_purchased 

        db.session.commit()
        return jsonify({
            'Message': f'User {customer_name} {customer_number} altered.'
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the user ID' })
        user = User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'Message': f'User {str(id)} deleted.'
        })


api.add_resource(HomePage, '/')
api.add_resource(CustomerManager, '/purchase_record')

if __name__ == '__main__':
    app.run(debug=True)