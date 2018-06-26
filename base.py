from api.views import app
import unittest
import json

class BaseClass(unittest.TestCase):

    """This is the base class for test cases."""

    

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.user_data = {"username": "Dee",
                     "fullname": "Didi Kashemwa",
                     "email": "didikashemwa@gmail.com",
                     "password": "yaay"
                     }
        
        self.ride_data = {
            'ride_id': 1,
            'driver_name': 'John Doe',
            'destination': 'Karen',
            'price': 250,
            'date': 16/6/2017,
            'time': 1800
        }

    def tearDown(self):
        """ Clear anything that has been saved. """
        pass 
