from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import random
import json
from api.models import User, Ride, Request

app = Flask(__name__)
api = Api(app)

users = []
rides =[]
requests =[]

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
        data = request.get_json()
        username = data['username']
        password = data['password']
        for user in users:
            if username == user.username:
                if password == user.password:
                    result = jsonify(
                        {"message": "You are successfully logged in"})
                    result.status_code = 200
                    return result
            else:
                result = jsonify({"message": "Wrong password or username."})
                result.status_code = 401
                return result


class RidesApi(Resource):
    def post(self):
        data = request.get_json
        ride_id=len(rides)+1,
        driver_name=data['driver_name'],destination =data['destination'], price=data['price'], date=data['date'], time=data['time']
        ride = Ride(ride_id=ride_id, driver_name=driver_name, destination=destination, price=price, date=date, time=time)

        rides.append(ride)

        result = jsonify({"message": "ride added"})
        result.status_code = 201
        return result

    def get(self, id=None):

        if id:
            for ride in rides:
                return {'ride': [ride.__dict__ for ride in rides if ride.ride_id==id]}
            return {'message':"Rides not found"}

        for ride in rides:
            return {'rides':[ride.__dict__ for ride in rides]}
        return {'message':"Rides not found"}
        


    # def get(self, ride_id=None):
    #     if ride_id != None:
    #         ride_items = [] #empty list to hold result
    #         print(ride_id)
    #         ride_items = [Ride for Ride in rides_list if Ride.ride_id == int(ride_id)]
    #         print(ride_items)
    #         if len(ride_items) < 1:
    #             return 'Item not found', 404
    #         return ({'ride': {'Id': ride_items[0].ride_id, 'driver': ride_items[0].driver_name, 'destination': ride_items[0].destination}},{'message':'Gets a specific ride'}), 200
    #     else:
    #         manyitems = []
    #         if len(rides_list) < 1:
    #             return 'rides not found', 404
    #         #looping through the list to print its contents
    #         for Ride in rides_list:
    #             manyitems.append(
    #                 {'ID': Ride.ride_id, 'title': Ride.driver_name, 'Destination': Ride.destination})
    #         return manyitems, 200
        


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
