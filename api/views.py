from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import random
import json

from api.models import User, Ride,Request, User_Schema, Ride_Schema, Request_Schema

app = Flask(__name__)
api = Api(app)

users = [User(username="Didi", fullname="Didi Kashemwa",
              email="didikashemwa@gmail.com", password="Yaay")]
rides = [Ride(ride_id=1234, driver_name="John Doe",
              destination="Karen", price=250, date=12/12/18, time=1830)]
requests = [Request(ride_id=1234, customer_name="Jane Doe",
              destination="Karen", price=250, date=12/12/18, time=1830)]

class UserSignupApi(Resource):
    def post(self):
        user=request.get_json
        if user.get('username') is None or user.get('fullname') is None or user.get ('email') or user.get('password') is None:
            result = jsonify({'message': 'All fields required'}) 
            result.status_code=400
            return  result

        u = User(username=user.get('username'), fullname=user.get('fullname'), email=user.get('email'), password=user.get('password'))

        users.append(u)

        result = jsonify({'message': 'Successfully registered'})
        result.status_code = 201
        return result




# class RidesApi(Resource):
#     def post(self):
#         rides = request.get_json()
#         r = Ride(ride_id=rides.get('ride_id'), driver_name=rides.get('driver_name'), destination=rides.get(
#             'destination'), price=rides.get('price'), date=rides.get('date'), time=rides.get('time'))

#         rides.append(r)

#         result = jsonify({"message": "ride added"})
#         result.status_code = 201
#         return result

    # def get(self):
    #     ride = Ride_Schema(many = True)
    #     ride_items = ride.dump(rides)

        # result=jsonify()


api.add_resource(UserSignupApi, '/api/v1/user/signup')

# api.add_resource(RidesApi,'/api/v1/rides')


if __name__ == '__main__':

    app.run(debug=True)
