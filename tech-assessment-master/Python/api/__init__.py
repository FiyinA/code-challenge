# api/__init__.py

from flask import Flask, jsonify
from flask_RESTX import Resource, Api

# create an instantiation of the Flask app
app = Flask(__name__)

api = Api(app)

data = [
    {
        "firstName": "Carol",
        "lastName": "Danvers",
        "agel": 33,
        "address":
        {
            "streetAddress": "417 5th Avenue Apt 10B",
            "city": "New York",
            "state": "NY",
            "postalCode": "10016"
        },
        "phoneNumber": "2125551234"
    },
    {
        "firstName": "Tony",
        "lastName": "Stark",
        "age": 48,
        "address":
        {
            "streetAddress": "890 Fifth Avenue",
            "city": "New York",
            "state": "NY",
            "postalCode": "10021"
        },
        "phoneNumber": "2125554567"
    },
    {
        "firstName": "Steve",
        "lastName": "Rogers",
        "age": 93,
        "address":
        {
            "streetAddress": "890 Fifth Avenue",
            "city": "New York",
            "state": "NY",
            "postalCode": "10021"
        },
        "phoneNumber": "6781367092"
    }
]

orders = [
    {
        "CustomerID": "1",
        "order": "phone"
    },
     {
        "CustomerID": "2",
        "order": "books"
    },
     {
        "CustomerID": "3",
        "order": "car"
    },
]

# set environment config here
app.config.from_object('project.config.DevelopmentConfig')

class Health(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'You keep using that word. I do not think it means what you think it means.'
        }

class Yes (Resource):

    def post (self):
        for x in data:
            for y in orders:
                if x['customerID'] == y['CustomerID']:
                    j = x['orders'] = y['order']
                    return j

    def get(self):
        for x in data:
            return x

    def delete(self):
        for ind, x in enumerate (data):
            if x['item'] == input:
                Tem = data.pop (ind)
    
    def update (self,CID, order):
        for x in orders:
            if CID == x['CustomerID']:
                x['order'] = order 


api.add_resource(Yes, '/yes')
