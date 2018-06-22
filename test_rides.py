from api.views import app
import unittest
import json


class RidesTestCase(unittest.TestCase):
    """This is the class for rides test cases"""

    def setUp(self):
        """Creates the app as a test client"""
        self.app=app
        self.client = self.app.test_client()
        self.data = {
            'ride_id': 1,
            'driver_name': 'John Doe',
            'destination': 'Karen',
            'price': 250,
            'date': 16/6/2017,
            'time': 1800
        }

    def test_add_ride(self):
        """Test Api can add a ride()"""
        response = self.client.post(
            '/api/v1/rides', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "ride successfully added")
        self.assertEqual(response.status_code, 201)
