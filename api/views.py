from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import random
import json

from api.models import User, Ride, Request, User_Schema, Ride_Schema, Request_Schema

app = Flask(__name__)
api = Api(app)

rides_list=[]# List to hold dummy ride data

users = [User(username="Dee", fullname="Didi Kashemwa",
              email="didikashemwa@gmail.com", password="Yaay")]

#creating 3 dummy users using the init method in models that takes 6 positional arguments
ride1 = Ride(3, "Celina Maka", "Kando",250, "12/12/18", 1835)
ride3 = Ride(5, "Su mbarika", "Simjui",250, "12/12/18", 1835)
ride4 = Ride(6, "Kamade mende", "Mtaa",250, "12/12/18", 1835)

#adding the dummy rides to the list
rides_list.append(ride1)
rides_list.append(ride3)
rides_list.append(ride4)


requests = [Request(ride_id=123, customer_id=234)]


class UserSignupApi(Resource):
    def post(self):
        user = request.get_json()
        if not user['username'] or not user['fullname'] or not user['email'] or not user['password']:
            result = jsonify({'message': 'All fields required'})
            result.status_code = 400
            return result

        u = User(user['username'], user['fullname'],
                 user['email'], user['password'])

        users.append(u)

        result = jsonify({"message": "Successfully registered"})
        result.status_code = 201
        return result


class UserLoginApi(Resource):
    def post(self):
        access = request.get_json()
        username = access['username']
        password = access['password']
        for user in users:
            if username == user.username:
                if password == user.password:
                    result = jsonify(
                        {"message": "You are successfully logged in"})
                    result.status_code = 200
                    return result
            else:
                result = jsonify({"message": 'Wrong password or username.'})
                result.status_code = 401
                return result


class RidesApi(Resource):
    def post(self):
        new_rides = request.get_json()
        r = Ride(new_rides['ride_id'], new_rides['driver_name'], new_rides['destination'],
                 new_rides['price'], new_rides['date'], new_rides['time'])

        #rides_list holds ride info it is our dummy database
        rides_list.append(r)

        result = jsonify({"message": "ride added"})
        result.status_code = 201
        return result

    def get(self, ride_id=None):
        if ride_id != None:
            ride_items = [] #empty list to hold result
            print(ride_id)
            ride_items = [Ride for Ride in rides_list if Ride.ride_id == int(ride_id)]
            print(ride_items)
            if len(ride_items) < 1:
                return 'Item not found', 404
            return ({'ride': {'Id': ride_items[0].ride_id, 'driver': ride_items[0].driver_name, 'destination': ride_items[0].destination}},{'message':'Gets a specific ride'}), 200
        else:
            manyitems = []
            if len(rides_list) < 1:
                return 'rides not found', 404
            #looping through the list to print its contents
            for Ride in rides_list:
                manyitems.append(
                    {'ID': Ride.ride_id, 'title': Ride.driver_name, 'Destination': Ride.destination})
            return manyitems, 200
        


class RequestRideApi(Resource):
    def post(self):
        req = request.get_json()
        ride_id = req['ride_id']
        customer_id = req['customer_id']

        r = Request(
            ride_id=ride_id,
            customer_id=customer_id
        )

        requests.append(r)

        return {"message": "Ride requested"}, 201


api.add_resource(UserSignupApi, '/api/v1/user/signup')
api.add_resource(UserLoginApi, '/api/v1/user/login')
api.add_resource(RidesApi, '/api/v1/rides/<int:ride_id>', '/api/v1/rides/')
api.add_resource(RequestRideApi, '/api/v1/request')


if __name__ == '__main__':

    app.run(debug=True)
