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
    email = fields.Str()
    password = fields.Str()
    

