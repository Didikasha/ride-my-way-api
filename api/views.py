from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import random
import json

from api.models import User, Ride,Request, User_Schema, Ride_Schema, Request_Schema

app = Flask(__name__)
api = Api(app)

users = [User(username="Dee", fullname="Didi Kashemwa",
              email="didikashemwa@gmail.com", password="Yaay")]
rides = [Ride(ride_id=1234, driver_name="John Doe",
              destination="Karen", price=250, date="12/12/18", time=1830)]
requests = [Request(ride_id=1234, customer_name="Jane Doe",
              destination="Karen", price=250, date="12/12/18", time=1830)]

class UserSignupApi(Resource):
    def post(self):
        user=request.get_json()
        if not user['username']  or not user['fullname'] or not user['email'] or not user['password']:
            result = jsonify({'message': 'All fields required'}) 
            result.status_code=400
            return result

        u = User(user['username'], user['fullname'],user['email'], user['password'])

        users.append(u)

        result = jsonify({"message": "Successfully registered"})
        result.status_code = 201
        return result

class UserLoginApi(Resource):
    def post (self):
        access = request.get_json()
        username = access['username']
        password = access['password']
        for user in users:
            if username == user.username:
                if password ==user.password:
                    result = jsonify({"message": "You are successfully logged in"})
                    result.status_code = 200
                    return result
            else:
                result = jsonify({"message": 'Wrong password or username.'})
                result.status_code = 401
                return result



class RidesApi(Resource):
    def post(self):
        new_rides = request.get_json()
        r = Ride(new_rides['ride_id'], new_rides['driver_name'],new_rides['destination'], new_rides['price'], new_rides['date'], new_rides['time'])

        rides.append(r)

        result = jsonify({"message": "ride added"})
        result.status_code = 201
        return result

    def get(self):
        # ride = Ride_Schema(many = True)
        # ride_items = ride.dump(rides)
        # result=jsonify(ride_items)
        itemlist=[]
        for item in rides:
            itemlist.append({"Ride Id":item.ride_id, "Driver name": item.driver_name , "destination": item.destination})
        return itemlist


api.add_resource(UserSignupApi, '/api/v1/user/signup')
api.add_resource(UserLoginApi, '/api/v1/user/login')
api.add_resource(RidesApi,'/api/v1/rides')


if __name__ == '__main__':

    app.run(debug=True)
