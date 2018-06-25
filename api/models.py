from marshmallow import Schema, fields
import random

class User():
    def __init__(self,username, fullname, email, password):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.password = password

class User_Schema(Schema):
    username = fields.Str()
    fullname = fields.Str()
    email = fields.Str()
    password = fields.Str()

class Ride():
    def __init__(self, ride_id, driver_name, destination, price, date, time):
        self.ride_id = random.randint(1,100)
        self.driver_name = driver_name
        self.destination = destination
        self.price = price
        self.date = date
        self.time = time

class Ride_Schema():
    ride_id=fields.Int()
    driver_name = fields.Str()
    destination = fields.Str()
    price= fields.Int()
    date = fields.Int()
    time = fields.Int()

class Request():
    def __init__(self,ride_id, customer_name, destination, price, date, time):
        self.ride_id = random.randint(1,100)
        self.customer_name = customer_name
        self.destination = destination
        self.price = price
        self.date = date
        self.time = time

class Request_Schema():
    ride_id=fields.Int()
    customer_name = fields.Str()
    destination = fields.Str()
    price= fields.Int()
    date = fields.Int()
    time = fields.Int()




